import fitz
import docx

def extract_text_from_pdf(filename):
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)