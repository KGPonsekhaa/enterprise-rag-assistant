# RAG pipeline logic
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.logger import logger


def create_chunks(documents):
    """
    Create chunks while preserving document metadata.
    """

    logger.info("=" * 60)
    logger.info("Creating Chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    all_chunks = []

    for document in documents:

        source = document["source"]
        text = document["text"]

        chunks = splitter.split_text(text)

        logger.info("-" * 50)
        logger.info(f"{source}")
        logger.info(f"Chunks Created : {len(chunks)}")

        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": source
            })

    logger.info("=" * 60)
    logger.info(f"Total Chunks Created : {len(all_chunks)}")
    logger.info("Chunk Creation Completed")

    return all_chunks