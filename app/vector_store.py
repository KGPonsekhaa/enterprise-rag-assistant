# Vector database logic
import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.logger import logger

load_dotenv()


def create_vector_store(chunks):
    logger.info("=" * 60)
    logger.info("Creating Vector Store...")
    logger.info(f"Total Chunks : {len(chunks)}")
    logger.info("Generating Azure OpenAI Embeddings...")
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )

    logger.info(f"Generating embeddings for {len(chunks)} chunks...")
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )
    logger.info("FAISS Vector Store Created Successfully")
    logger.info("Vector Store Ready")

    return vector_store