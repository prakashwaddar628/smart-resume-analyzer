import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from jd_parser import extract_skills_from_jd, filter_tech_skills
from matcher import match_skills
from feedback import generate_feedback
from recommender import get_course_links

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
resume_txt = ""
resume_tech_skills = []

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
tech_skills = []

if job_description_text:
    st.markdown("### ✨ Extracted Job Description:")
    st.text_area("JD Text", job_description_text, height=300)

    jd_skills = extract_skills_from_jd(job_description_text)
    tech_skills = filter_tech_skills(jd_skills)

    st.markdown("### 🧠 Extracted Key Technical Skills from JD:")
    st.write(tech_skills)

# -------------------------------
# 📥 Extract Resume Skills
# -------------------------------
if resume_txt:
    resume_skills = extract_skills_from_jd(resume_txt)
    resume_tech_skills = filter_tech_skills(resume_skills)

    st.markdown("### 📌 Extracted Key Technical Skills from Resume:")
    st.write(resume_tech_skills)

# -------------------------------
# 📊 Resume vs JD Skill Matching
# -------------------------------
if resume_tech_skills and tech_skills:
    st.markdown("---")
    st.header("📊 Resume vs JD Skill Matching")

    result = match_skills(resume_tech_skills, tech_skills)

    st.markdown(f"✅ **Match Score:** `{result['match_score']}%`")
    st.progress(int(result['match_score']))

    st.markdown("🟢 **Matching Skills:**")
    st.write(result['matched_skills'])

    st.markdown("🔴 **Missing Skills (JD but not in Resume):**")
    st.write(result['missing_skills'])

    st.markdown("🧠 **AI Feedback & Recommendations:**")
    feedback = generate_feedback(result['missing_skills'])
    st.markdown(feedback)

    course_links = get_course_links(result['missing_skills'])
    if course_links:
        st.markdown("🎓 **Recommended Learning Resources (Free & Paid):**")
        for skill, links in course_links.items():
            st.markdown(f"- **{skill.title()}**")
            if "free" in links:
                st.markdown(f"    - 🆓 [Free Course]({links['free']})")
            if "paid" in links:
                st.markdown(f"    - 💰 [Paid Course]({links['paid']})")

elif job_description_text and not resume_txt:
    st.warning("⚠️ Please upload your resume to start matching.")

elif resume_txt and not job_description_text:
    st.warning("⚠️ Please provide a job description to match with your resume.")

elif resume_txt and job_description_text and (not resume_tech_skills or not tech_skills):
    st.warning("⚠️ Could not extract skills properly from resume or JD. Please check the content.")
