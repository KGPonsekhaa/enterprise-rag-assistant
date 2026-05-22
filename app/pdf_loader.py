# PDF loading logic
import fitz

def load_pdf(pdf_path: str) -> str:
    """
    Load PDF and extract text
    """
    document = fitz.open(pdf_path)
    full_text = ""

    for page in document:
        full_text += page.get_text()

    return full_text

