from fastapi import FastAPI
from app.pdf_loader import load_pdf
from app.rag_pipeline import create_chunks
from app.vector_store import create_vector_store

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

@app.get("/")
def home():

    pdf_text = load_pdf("data/sample.pdf")
    chunks = create_chunks(pdf_text)
    vector_store = create_vector_store(chunks)


    return {
        "message": "FAISS Vector Store Created Successfully",
        "total_chunks": len(chunks)
    }