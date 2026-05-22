from fastapi import FastAPI
from app.pdf_loader import load_pdf
from app.rag_pipeline import create_chunks

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

@app.get("/")
def home():

    pdf_text = load_pdf("data/sample.pdf")

    chunks = create_chunks(pdf_text)

    return {
        "message": "Chunking Completed Successfully",
        "total_characters": len(pdf_text),
        "total_chunks": len(chunks),
        "first_chunk_preview": chunks[0][:300]
    }