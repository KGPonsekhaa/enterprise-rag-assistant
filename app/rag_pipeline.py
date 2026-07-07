# RAG pipeline logic
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.logger import logger

def create_chunks(text: str):
    logger.info("=" * 60)
    logger.info("Creating Chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)
    total_characters = sum(len(chunk) for chunk in chunks)

    logger.info(f"Total Chunk Characters : {total_characters}")
    logger.info(f"Chunk Size : 1000")
    logger.info(f"Chunk Overlap : 200")
    logger.info(f"Total Chunks Created : {len(chunks)}")
    logger.info("Chunk Creation Completed")
    return chunks