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

# Custom CSS
st.markdown("""
    <style>
        body { background-color: #f4f6f9; }
        .block-container { padding: 2rem 2rem 2rem 2rem; }
        .stTextArea textarea { font-size: 15px; font-family: 'Segoe UI'; }
        .stButton button { color: green; font-weight: bold; border: 2px solid green; }
        .stRadio > div { flex-direction: row; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Smart Resume Analyzer")
    st.markdown("Version 1.0")
    st.markdown("Built by [Prakash](https://github.com/prakashwaddar628)")
    st.markdown("[GitHub Repo](https://github.com/prakashwaddar628/smart_resume_analyzer)")

st.title("Smart Resume Analyzer")
st.markdown("### Upload your resume and job description to analyze skills and get tailored feedback & learning paths.")

# Create uploads folder
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Layout
col1, col2 = st.columns(2)

# Resume Upload
resume_txt = ""
with col1:
    st.subheader("Resume Upload")
    upload_file = st.file_uploader("Upload Resume (.docx or .pdf)", type=["pdf", "docx"])
    if upload_file:
        filepath = os.path.join("uploads", upload_file.name)
        with open(filepath, "wb") as f:
            f.write(upload_file.getbuffer())
        try:
            resume_txt = extract_text_from_pdf(filepath) if upload_file.name.endswith(".pdf") else extract_text_from_docx(filepath)
            with open("./uploads/resume.txt", "w", encoding="utf-8") as f:
                f.write(resume_txt)
            st.success("Resume parsed successfully!")
            st.text_area("Resume Text", resume_txt, height=300)
        except Exception as e:
            st.error(f"Error extracting resume text: {e}")

# Job Description Input
job_description_text = ""
with col2:
    st.subheader("Job Description")
    jd_input_method = st.radio("Provide JD via:", ("Paste Text", "Upload File"))
    if jd_input_method == "Paste Text":
        job_description_text = st.text_area("Paste Job Description", height=300)
    elif jd_input_method == "Upload File":
        jd_file = st.file_uploader("Upload JD (.txt or .pdf)", type=["txt", "pdf"], key="jd_file")
        if jd_file:
            jd_path = os.path.join("uploads", jd_file.name)
            with open(jd_path, "wb") as f:
                f.write(jd_file.getbuffer())
            try:
                job_description_text = extract_text_from_pdf(jd_path) if jd_file.name.endswith(".pdf") else jd_file.read().decode("utf-8")
                st.text_area("JD Text", job_description_text, height=300)
            except Exception as e:
                st.error(f"Error extracting JD text: {e}")

# Action Button
analyze = st.button("Analyze")

# Run Analysis on Click
if analyze:
    technical_skills_jd = []
    technical_skills_resume = []

    if not resume_txt or not job_description_text:
        st.warning("Please upload both resume and job description.")
    else:
        try:
            # Extract Skills
            jd_skills = extract_skills_from_jd(job_description_text)
            resume_skills = extract_skills_from_jd(resume_txt)
            technical_skills_jd = filter_tech_skills(jd_skills)
            technical_skills_resume = filter_tech_skills(resume_skills)

            # Display Skills
            st.markdown("#### Extracted JD Skills")
            st.success(", ".join(technical_skills_jd) if technical_skills_jd else "No technical skills found.")

            st.markdown("#### Extracted Resume Skills")
            st.info(", ".join(technical_skills_resume) if technical_skills_resume else "No technical skills found.")

            # Match
            if technical_skills_jd and technical_skills_resume:
                result = match_skills(technical_skills_resume, technical_skills_jd)

                st.markdown("---")
                st.header("Skill Matching Report")
                col3, col4 = st.columns([1, 4])
                col3.metric("Match Score", f"{result['match_score']}%")
                col4.progress(int(result['match_score']))

                st.markdown("#### Matching Skills")
                st.success(", ".join(result['matched_skills']) or "None")

                st.markdown("#### Missing Skills")
                st.error(", ".join(result['missing_skills']) or "None")

                st.markdown("### AI Suggestions")
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

            else:
                st.warning("Skills could not be extracted properly.")

        except Exception as e:
            st.error(f"Error during analysis: {e}")

st.markdown("---")
st.markdown("<center>© 2025 Prakash | All Rights Reserved</center>", unsafe_allow_html=True)
