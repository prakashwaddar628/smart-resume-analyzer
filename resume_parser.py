import pdfplumber
import docx

def extract_text_from_pdf(filename):
    text = ""
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_text_from_docx(file):
    doc = docx.Document(file)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)
