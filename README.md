# enterprise-rag-assistant
Enterprise RAG assistant using LangChain, FAISS, Azure OpenAI, and conversational memory
# Enterprise RAG Assistant 🚀

Enterprise-grade Retrieval-Augmented Generation (RAG) Assistant built using FastAPI, LangChain, Azure OpenAI, FAISS, and LangSmith tracing.

This system ingests enterprise PDF documents, creates semantic embeddings, stores vectors in FAISS, retrieves relevant context using similarity search, and generates grounded answers using Azure OpenAI GPT-4o-mini.

---

# Features

✅ PDF ingestion pipeline  
✅ Recursive text chunking  
✅ Azure OpenAI embeddings  
✅ FAISS vector database  
✅ Semantic retrieval  
✅ Grounded GPT responses  
✅ LangSmith tracing  
✅ Modular FastAPI backend  

---

# Architecture

```text
User Question
      ↓
PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Azure OpenAI Embeddings
      ↓
FAISS Vector Store
      ↓
Semantic Retrieval
      ↓
GPT-4o-mini
      ↓
Grounded Answer
```

---

# Tech Stack

- FastAPI
- LangChain
- Azure OpenAI
- FAISS
- LangSmith
- Python

---

# Project Structure

```text
enterprise-rag-assistant/
│
├── app/
│   ├── main.py
│   ├── pdf_loader.py
│   ├── rag_pipeline.py
│   ├── vector_store.py
│   ├── prompt_builder.py
│   ├── config.py
│   └── utils.py
│
├── data/
├── screenshots/
├── .env.example
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/KGPonsekhaa/enterprise-rag-assistant.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
LANGSMITH_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=
LANGSMITH_PROJECT=

AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=

AZURE_OPENAI_CHAT_DEPLOYMENT=
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=
```

---

# Run Application

```bash
uvicorn app.main:app --reload --port 8001
```

---

# API Endpoint

## Ask Questions

```http
GET /ask?question=your_question
```

Example:

```text
http://127.0.0.1:8001/ask?question=What is the purpose of this document?
```

---

# Sample Output

```json
{
  "question": "What is the purpose of this document?",
  "answer": "The document provides information about procedures used to optimize supply and market planning decisions."
}
```

---

# LangSmith Tracing

Integrated LangSmith tracing for:
- prompt observability
- debugging
- retrieval monitoring
- LLM execution tracing

---

# Future Enhancements

- Conversational memory
- Multi-PDF upload
- Hybrid search (BM25 + FAISS)
- Citation support
- Streaming responses
- Chat UI
- Multi-agent workflows

---

# Author

Ponsekhaa K G  
Generative AI Engineer
