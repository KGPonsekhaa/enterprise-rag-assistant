from fastapi import FastAPI
from app.pdf_loader import load_pdf

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

@app.get("/")
def home():

    pdf_text = load_pdf("data/sample.pdf")

    return {
        "message": "PDF Loaded Successfully",
        "characters": len(pdf_text)
    }