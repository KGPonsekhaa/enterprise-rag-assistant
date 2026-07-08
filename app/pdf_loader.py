# PDF loading logic
import os
import fitz
from app.logger import logger


def load_all_pdfs(data_folder: str):
    """
    Load all PDF files from the data folder.
    Returns:
        [
            {
                "source": "sample.pdf",
                "text": "..."
            },
            ...
        ]
    """

    documents = []

    logger.info("=" * 60)
    logger.info("Loading PDF Documents...")

    for filename in os.listdir(data_folder):

        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(data_folder, filename)

        logger.info("-" * 50)
        logger.info(f"Loading: {filename}")

        document = fitz.open(pdf_path)

        full_text = ""

        for page in document:
            full_text += page.get_text()

        total_pages = len(document)
        document.close()

        logger.info(f"Pages : {total_pages}")
        logger.info(f"Characters : {len(full_text)}")

        documents.append({
            "source": filename,
            "text": full_text
        })

    logger.info("=" * 60)
    logger.info(f"Total PDF Documents Loaded : {len(documents)}")

    return documents