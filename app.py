import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_text_from_docx

st.set_page_config(page_title="Smart Resume Analyzer")
st.title("Smart Resume Analyzer")
st.markdown("Upload your resume and extract text content for analysis.")

if not os.path.exists("uploads"):
    os.makedirs("uploads")

upload_file = st.file_uploader("Upload Resume (.docx or .pdf)", type=["pdf", "docx"])

if upload_file:
    filepath = os.path.join("uploads", upload_file.name)

    with open (filepath, "wb") as f:
        f.write(upload_file.getbuffer())

    if upload_file.name.endswith(".pdf"):
        resume_txt = extract_text_from_pdf(filepath)
    else:
        resume_txt = extract_text_from_docx(filepath)

    st.subheader("Extracted Resume Text:")
    st.text_area("Text Output",resume_txt, height=400)

    with open("./uploads/resume.txt", "w", encoding="utf-8") as f:
        f.write(resume_txt)
    
    st.success("Text extracted and saved successfully!")