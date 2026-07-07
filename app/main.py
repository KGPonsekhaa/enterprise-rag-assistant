from fastapi import FastAPI
from app.pdf_loader import load_pdf
from app.rag_pipeline import create_chunks
from app.vector_store import create_vector_store
from app.prompt_builder import generate_response
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

pdf_text = load_pdf("data/sample.pdf")
chunks = create_chunks(pdf_text)
vector_store = create_vector_store(chunks)

logger.info("Enterprise RAG Assistant Ready")
logger.info("=" * 60)


@app.get("/ask")
def ask_question(question: str):

    overall_start = time.time()

    logger.info("=" * 60)
    logger.info("Enterprise RAG Pipeline Started")
    logger.info(f"User Query : {question}")

    # Retrieve Relevant Chunks
    docs = vector_store.similarity_search_with_score(
        question,
        k=3
    )

    logger.info("=" * 60)
    logger.info("Retrieval Results")
    logger.info(f"Retrieved Chunks : {len(docs)}")

    context_chunks = []

    for i, (doc, score) in enumerate(docs, start=1):

        logger.info(f"Chunk {i}")
        logger.info(f"Similarity Score : {score:.4f}")
        logger.info(doc.page_content[:150])

        context_chunks.append(doc.page_content)

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

    return {
        "question": question,
        "answer": answer,
        "performance_metrics": {
            "retrieved_chunks": len(docs),
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
