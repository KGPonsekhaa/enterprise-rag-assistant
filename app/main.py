from fastapi import FastAPI
from app.pdf_loader import load_pdf
from app.rag_pipeline import create_chunks
from app.vector_store import create_vector_store
from app.prompt_builder import generate_response

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

@app.get("/ask")
def ask_question(question: str):

    pdf_text = load_pdf("data/sample.pdf")
    chunks = create_chunks(pdf_text)
    vector_store = create_vector_store(chunks)
    docs = vector_store.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    answer = generate_response(context, question)
    return {
        "question": question,
        "answer": answer
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
