from fastapi import FastAPI
from app.pdf_loader import load_all_pdfs
from app.rag_pipeline import create_chunks
from app.vector_store import create_vector_store
from app.prompt_builder import generate_response
from app.context_isolation import ContextIsolationFramework
from app.logger import logger
import time

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

# ==========================================================
# Initialize RAG Components Once (Application Startup)
# ==========================================================

logger.info("=" * 60)
logger.info("Initializing Enterprise RAG Assistant...")

documents = load_all_pdfs("data")
chunks = create_chunks(documents)
vector_store = create_vector_store(chunks)
context_isolation = ContextIsolationFramework()

logger.info("Enterprise RAG Assistant Ready")
logger.info("=" * 60)


@app.get("/ask")
def ask_question(question: str):

    overall_start = time.time()

    logger.info("=" * 60)
    logger.info("Enterprise RAG Pipeline Started")
    logger.info(f"User Query : {question}")

    # Retrieve Relevant Chunks
    docs = vector_store.similarity_search_with_score(question, k=3)
    logger.info("=" * 60)
    logger.info("Retrieval Results")
    logger.info(f"Retrieved Chunks : {len(docs)}")

    context_chunks = []
    retrieved_sources = []

    for i, (doc, score) in enumerate(docs, start=1):

        source = doc.metadata.get("source", "Unknown")

        logger.info("-" * 50)
        logger.info(f"Chunk {i}")
        logger.info(f"Source : {source}")
        logger.info(f"Similarity Score : {score:.4f}")
        logger.info(doc.page_content[:200])

        context_chunks.append(doc.page_content)

        retrieved_sources.append({
            "document": source,
            "similarity_score": round(score, 4)
        })

    context = "\n".join(context_chunks)
    logger.info(f"Context Characters : {len(context)}")
    logger.info("Context Preview:")
    logger.info(context[:300])

    # Generate Response
    result = generate_response(context, question)

    answer = result["answer"]
    performance_metrics = result["performance_metrics"]

    overall_end = time.time()

    logger.info("=" * 60)
    logger.info(f"Total Pipeline Time : {overall_end - overall_start:.2f} sec")
    logger.info("Enterprise RAG Pipeline Completed Successfully")
    logger.info("=" * 60)

    documents_used = sorted({
        doc.metadata.get("source", "Unknown")
        for doc, _ in docs
    })

    return {
        "question": question,
        "answer": answer,
        "retrieval_summary": {
            "retrieved_chunks": len(docs),
            "documents_used": documents_used
        },
        "performance_metrics": {
            "context_size_characters": len(context),
            "prompt_tokens": performance_metrics["prompt_tokens"],
            "completion_tokens": performance_metrics["completion_tokens"],
            "total_tokens": performance_metrics["total_tokens"],
            "llm_response_time": f'{performance_metrics["llm_response_time"]:.2f} sec',
            "pipeline_time": f'{overall_end - overall_start:.2f} sec'
        }
    }

# @app.get("/")
# def home():

#     pdf_text = load_pdf("data/sample.pdf")
#     chunks = create_chunks(pdf_text)
#     vector_store = create_vector_store(chunks)
#     query = "What is the purpose of this document?"

#     docs = vector_store.similarity_search(query, k=3)
#     results = []

#     for doc in docs:
#         results.append(doc.page_content[:500])

#     return {
#         "message": "Semantic Retrieval Working Successfully",
#         "retrieved_chunks": results
#     }
