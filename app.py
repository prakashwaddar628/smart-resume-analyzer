import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from jd_parser import extract_skills_from_jd, filter_tech_skills
from matcher import match_skills
from feedback import generate_feedback
from recommender import get_course_links
from dashboard import render_dashboard

# Page Configuration
st.set_page_config(page_title="Smart Resume Analyzer", page_icon="🧠", layout="wide")
st.markdown("""
    <style>
        .main { background-color: #ffffff; }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTextArea textarea { font-size: 15px; line-height: 1.6; }
        .stButton > button {
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
            border-radius: 6px;
        }
        .stRadio > div { gap: 10px; }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
            color: #212529;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Smart Resume Analyzer")
st.markdown("""
### 🎯 Resume vs Job Description Analyzer
Easily analyze your resume against a job description to:
- 🔍 Identify skill gaps
- 💬 Receive AI-based feedback
- 📚 Get personalized course recommendations
""")

if not os.path.exists("uploads"):
    os.makedirs("uploads")

# -------------------------------
# 📄 Resume Upload & Extraction
# -------------------------------
st.markdown("---")
st.header("📄 Step 1: Upload Your Resume")

resume_txt = ""
resume_tech_skills = []

upload_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["pdf", "docx"])

if upload_file:
    filepath = os.path.join("uploads", upload_file.name)
    with open(filepath, "wb") as f:
        f.write(upload_file.getbuffer())

    resume_txt = extract_text_from_pdf(filepath) if filepath.endswith(".pdf") else extract_text_from_docx(filepath)

    st.success("✅ Resume uploaded and parsed!")
    st.markdown("#### 📃 Extracted Resume Text")
    st.text_area("Resume Output", resume_txt, height=250)

    with open("./uploads/resume.txt", "w", encoding="utf-8") as f:
        f.write(resume_txt)

# -------------------------------
# 🧾 Job Description Input
# -------------------------------
st.markdown("---")
st.header("🧾 Step 2: Add Job Description")

jd_input_method = st.radio("Choose input method:", ("Paste Text", "Upload File"))
job_description_text = ""

if jd_input_method == "Paste Text":
    job_description_text = st.text_area("Paste the job description below:", height=250)

elif jd_input_method == "Upload File":
    jd_file = st.file_uploader("Upload JD File (.txt or .pdf)", type=["txt", "pdf"], key="jd_file")
    if jd_file:
        jd_path = os.path.join("uploads", jd_file.name)
        with open(jd_path, "wb") as f:
            f.write(jd_file.getbuffer())

        job_description_text = extract_text_from_pdf(jd_path) if jd_file.name.endswith(".pdf") else jd_file.read().decode("utf-8")

# -------------------------------
# 🧠 JD Parsing and Skill Extraction
# -------------------------------
tech_skills = []

if job_description_text:
    st.markdown("#### ✨ Extracted Job Description")
    st.text_area("Job Description Output", job_description_text, height=250)

    jd_skills = extract_skills_from_jd(job_description_text)
    tech_skills = filter_tech_skills(jd_skills)

    st.markdown("#### 🧠 Key Technical Skills from JD")
    st.write(tech_skills)

# -------------------------------
# 📥 Extract Resume Skills
# -------------------------------
if resume_txt:
    resume_skills = extract_skills_from_jd(resume_txt)
    resume_tech_skills = filter_tech_skills(resume_skills)

    st.markdown("#### 📌 Key Technical Skills from Resume")
    st.write(resume_tech_skills)

# -------------------------------
# 📊 Resume vs JD Skill Matching
# -------------------------------
if resume_tech_skills and tech_skills:
    st.markdown("---")
    st.header("📊 Step 3: Skill Matching & Insights")

    result = match_skills(resume_tech_skills, tech_skills)

    st.metric(label="✅ Match Score", value=f"{result['match_score']}%")
    st.progress(int(result['match_score']))

    st.markdown("#### 🟢 Matching Skills")
    st.write(result['matched_skills'])

    st.markdown("#### 🔴 Missing Skills")
    st.write(result['missing_skills'])

    st.markdown("---")
    st.subheader("🤖 AI Feedback & Recommendations")

    feedback = generate_feedback(result['missing_skills'])
    st.info(feedback)

    course_links = get_course_links(result['missing_skills'])
    if course_links:
        st.markdown("### 🎓 Personalized Learning Resources")
        for skill, links in course_links.items():
            st.markdown(f"**{skill.title()}**")
            if "free" in links:
                st.markdown(f"- 🆓 [Free Course]({links['free']})")
            if "paid" in links:
                st.markdown(f"- 💰 [Paid Course]({links['paid']})")

    render_dashboard(result)

elif job_description_text and not resume_txt:
    st.warning("⚠️ Please upload your resume to start matching.")

elif resume_txt and not job_description_text:
    st.warning("⚠️ Please provide a job description to match with your resume.")

elif resume_txt and job_description_text and (not resume_tech_skills or not tech_skills):
    st.warning("⚠️ Could not extract skills properly from resume or JD. Please check the content.")
