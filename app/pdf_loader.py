# PDF loading logic
import fitz
from app.logger import logger


def load_pdf(pdf_path: str) -> str:
    """
    Load PDF and extract text
    """

    logger.info("=" * 60)
    logger.info("Loading PDF...")
    logger.info(f"PDF Path: {pdf_path}")

    document = fitz.open(pdf_path)
    full_text = ""
    
    page_count = len(document)

    for page in document:
        full_text += page.get_text()

    document.close()
    logger.info(f"Total Pages: {page_count}")
    logger.info(f"Characters Extracted: {len(full_text)}")
    logger.info("PDF Loaded Successfully")

    return full_text