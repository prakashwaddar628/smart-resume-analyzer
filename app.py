import streamlit as st
import os

from resume_parser import extract_text_from_pdf, extract_text_from_docx
from jd_parser import extract_skills_from_jd, filter_tech_skills
from matcher import match_skills
from feedback import generate_feedback
from recommender import get_course_links
from dashboard import render_dashboard

# Page Configuration
st.set_page_config(page_title="Smart Resume Analyzer", page_icon=":briefcase:", layout="wide")

# Custom CSS for cleaner UI
st.markdown("""
    <style>
        body { background-color: #f4f6f9; }
        .block-container { padding: 2rem 2rem 2rem 2rem; }
        .stTextArea textarea { font-size: 15px; font-family: 'Segoe UI'; }
        .stButton button { background-color: #4CAF50; color: white; font-weight: bold; }
        .stRadio > div { flex-direction: row; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Smart Resume Analyzer")
    st.markdown("Version 1.0")
    st.markdown("Built by [Prakash](https://github.com/prakashwaddar628)")
    st.markdown("[GitHub Repo](https://github.com/prakashwaddar628/smart_resume_analyzer)")

st.title("Smart Resume Analyzer")
st.markdown("### Upload your resume and job description to analyze skills and get tailored feedback & learning paths.")

if not os.path.exists("uploads"):
    os.makedirs("uploads")

# ---- Columns Layout ----
col1, col2 = st.columns(2)

# ------------ Resume Upload ------------
with col1:
    st.subheader("Resume Upload")
    resume_txt = ""
    resume_tech_skills = []

    upload_file = st.file_uploader("Upload Resume (.docx or .pdf)", type=["pdf", "docx"])
    if upload_file:
        filepath = os.path.join("uploads", upload_file.name)
        with open(filepath, "wb") as f:
            f.write(upload_file.getbuffer())

        try:
            if upload_file.name.endswith(".pdf"):
                resume_txt = extract_text_from_pdf(filepath)
            else:
                resume_txt = extract_text_from_docx(filepath)

            with open("./uploads/resume.txt", "w", encoding="utf-8") as f:
                f.write(resume_txt)

            st.success("Resume parsed successfully!")
            st.text_area("Resume Text", resume_txt, height=300)

        except Exception as e:
            st.error(f"Error extracting resume text: {e}")

# ------------ Job Description Input ------------
with col2:
    st.subheader("Job Description")
    jd_input_method = st.radio("Provide JD via:", ("Paste Text", "Upload File"))
    job_description_text = ""

    if jd_input_method == "Paste Text":
        job_description_text = st.text_area("Paste Job Description", height=300)

    elif jd_input_method == "Upload File":
        jd_file = st.file_uploader("Upload JD (.txt or .pdf)", type=["txt", "pdf"], key="jd_file")
        if jd_file:
            jd_path = os.path.join("uploads", jd_file.name)
            with open(jd_path, "wb") as f:
                f.write(jd_file.getbuffer())
            try:
                if jd_file.name.endswith(".pdf"):
                    job_description_text = extract_text_from_pdf(jd_path)
                else:
                    job_description_text = jd_file.read().decode("utf-8")
            except Exception as e:
                st.error(f"Error extracting JD text: {e}")

    if job_description_text:
        st.text_area("JD Text", job_description_text, height=300)

# ------------ Extract Skills ------------
technical_skills_jd = []
technical_skills_resume = []

if job_description_text:
    try:
        jd_skills = extract_skills_from_jd(job_description_text)
        technical_skills_jd = filter_tech_skills(jd_skills)
        st.markdown("#### Extracted JD Skills")
        st.success(", ".join(technical_skills_jd) if technical_skills_jd else "No technical skills found.")
    except Exception as e:
        st.error(f"JD Skill Extraction Error: {e}")

if resume_txt:
    try:
        resume_skills = extract_skills_from_jd(resume_txt)
        technical_skills_resume = filter_tech_skills(resume_skills)
        st.markdown("#### Extracted Resume Skills")
        st.info(", ".join(technical_skills_resume) if technical_skills_resume else "No technical skills found.")
    except Exception as e:
        st.error(f"Resume Skill Extraction Error: {e}")

# ------------ Matching & Feedback ------------
if technical_skills_jd and technical_skills_resume:
    st.markdown("---")
    st.header("Skill Matching Report")

    try:
        result = match_skills(technical_skills_resume, technical_skills_jd)

        col3, col4 = st.columns([1, 4])
        with col3:
            st.metric(label="Match Score", value=f"{result['match_score']}%")
        with col4:
            st.progress(int(result['match_score']))

        st.markdown("#### Matching Skills")
        st.success(", ".join(result['matched_skills']) or "None")

        st.markdown("#### Missing Skills")
        st.error(", ".join(result['missing_skills']) or "None")

        st.markdown("---")
        st.subheader("AI Suggestions")
        st.write(generate_feedback(result['missing_skills']))

        course_links = get_course_links(result['missing_skills'])
        if course_links:
            st.markdown("### Recommended Resources")
            for skill, links in course_links.items():
                st.markdown(f"**{skill.title()}**")
                if "free" in links:
                    st.markdown(f"- [Free Course]({links['free']})")
                if "paid" in links:
                    st.markdown(f"- [Paid Course]({links['paid']})")

        render_dashboard(result)

    except Exception as e:
        st.error(f"Skill Matching Error: {e}")

elif job_description_text and not resume_txt:
    st.warning("Please upload your resume.")

elif resume_txt and not job_description_text:
    st.warning("Please provide a job description.")

elif resume_txt and job_description_text and (not technical_skills_resume or not technical_skills_jd):
    st.warning("Skills could not be extracted from resume or JD. Please ensure content is clear.")

st.markdown("---")
st.markdown("<center>© 2025 Prakash | All Rights Reserved</center>", unsafe_allow_html=True)
