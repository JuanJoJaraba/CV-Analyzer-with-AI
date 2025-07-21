from pdfminer.high_level import extract_text
from docx import Document
import os

def extract_text_from_pdf(path):
    try:
        text = extract_text(path)
        return text.strip()
    except Exception as e:
        return f"Error al leer PDF: {e}"

def extract_text_from_docx(path):
    try:
        doc = Document(path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"Error al leer DOCX: {e}"

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        return "Formato no soportado. Usa PDF o DOCX."
