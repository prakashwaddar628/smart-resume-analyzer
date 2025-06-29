import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from jd_parser import extract_skills_from_jd, filter_tech_skills

# Page config
st.set_page_config(page_title="Smart Resume Analyzer")
st.title("🧠 Smart Resume Analyzer")
st.markdown("Upload your resume and a job description to extract relevant information for matching.")

# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# -------------------------------
# 📄 Resume Upload & Extraction
# -------------------------------
upload_file = st.file_uploader("📄 Upload Resume (.docx or .pdf)", type=["pdf", "docx"])

if upload_file:
    filepath = os.path.join("uploads", upload_file.name)

    with open(filepath, "wb") as f:
        f.write(upload_file.getbuffer())

    if upload_file.name.endswith(".pdf"):
        resume_txt = extract_text_from_pdf(filepath)
    else:
        resume_txt = extract_text_from_docx(filepath)

    st.subheader("📃 Extracted Resume Text:")
    st.text_area("Resume Text Output", resume_txt, height=400)

    with open("./uploads/resume.txt", "w", encoding="utf-8") as f:
        f.write(resume_txt)

    st.success("✅ Resume text extracted and saved!")

# -------------------------------
# 📄 Job Description Input
# -------------------------------
st.markdown("---")
st.subheader("🧾 Job Description Input")

jd_input_method = st.radio("How do you want to provide the JD?", ("Paste Text", "Upload File"))

job_description_text = ""

if jd_input_method == "Paste Text":
    job_description_text = st.text_area("Paste the job description here:", height=300)

elif jd_input_method == "Upload File":
    jd_file = st.file_uploader("Upload JD File (.txt or .pdf)", type=["txt", "pdf"], key="jd_file")
    if jd_file:
        jd_path = os.path.join("uploads", jd_file.name)
        with open(jd_path, "wb") as f:
            f.write(jd_file.getbuffer())

        if jd_file.name.endswith(".pdf"):
            job_description_text = extract_text_from_pdf(jd_path)
        else:
            job_description_text = jd_file.read().decode("utf-8")

# -------------------------------
# 🧠 JD Parsing and Skill Extraction
# -------------------------------
if job_description_text:
    st.markdown("### ✨ Extracted Job Description:")
    st.text_area("JD Text", job_description_text, height=300)

    skills = extract_skills_from_jd(job_description_text)
    tech_skills = filter_tech_skills(skills)
    st.markdown("### 🧠 Extracted Key Technical Skills from JD:")
    st.write(tech_skills)