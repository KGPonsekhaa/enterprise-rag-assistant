from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="Enterprise AI Assistant using RAG Architecture",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Assistant Running Successfully"
    }