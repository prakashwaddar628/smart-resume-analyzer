# 🧠 Smart Resume Analyzer

An AI-powered career tool to intelligently analyze your resume, compare it with job descriptions, and recommend personalized upskilling resources. Built with **Streamlit**, **spaCy**, and custom NLP matching logic.

---

## 📌 Project Overview

The Smart Resume Analyzer helps students and professionals improve their resumes for targeted job roles by:
- Extracting skill-related content from resumes
- Comparing it against any job description (JD)
- Highlighting skill gaps
- Recommending both free and paid resources to fill those gaps

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| UI | Streamlit |
| NLP | spaCy |
| Backend | Python |
| Skill Matching | Custom logic |
| Learning Links | Kaggle, Coursera, YouTube, Udemy, etc. |

---

## 🚀 Features by Phase

### ✅ Phase 1: Resume Text Extraction
- Upload `.pdf` or `.docx` resumes
- Extract and display clean text using `pdfminer` and `docx2txt`

### ✅ Phase 2: JD Skill Extraction
- Input JD via text box or upload
- Extract key skills using spaCy’s noun phrase extraction
- Filter for technical keywords

### ✅ Phase 3: Resume vs JD Skill Matching
- Compare extracted resume skills with JD skills
- Display:
  - Matching skills ✅
  - Missing skills ❌
  - Match percentage 📊

### ✅ Phase 4: GPT-like Feedback + Learning Suggestions
- Recommend courses for **missing skills**
- Include both **free** (Kaggle, YouTube, FreeCodeCamp) and **paid** (Coursera, Udemy, Microsoft Learn) resources
- Structured output with clickable learning paths

---

## 🎓 Sample Output

🧾 Job Description: Data Analyst Role at Flipkart

✅ Match Score: 68%

🟢 Matching Skills:
  -Python
  -SQL
  -Excel

🔴 Missing Skills:
  -Tableau
  -Power BI
  -Machine Learning

🎓 Recommended Courses:

-Tableau:
  Free: https://www.youtube.com/playlist?list=PLUaB...
  Paid: https://www.tableau.com/learn/training/20221
-Power BI:
Free: https://www.youtube.com/watch?v=AGrl-H87pRU
Paid: https://learn.microsoft.com/en-us/training/...
-Machine Learning:
Free: https://www.kaggle.com/learn/intro-to-machine-learning
Paid: https://www.coursera.org/learn/machine-learning

### 🧠 Phase 5: GPT Feedback, Skill Recommendations & Analytics Dashboard
In this phase, we enhanced the resume analyzer by adding AI-generated feedback, personalized course suggestions, and a data-driven analytics dashboard using Plotly.

🚀 Features Added
✅ 1. AI-Powered Resume Feedback
Uses GPT-based models to analyze missing skills.

Generates smart, actionable feedback for candidates to improve their resume.

🎓 2. Skill-Based Course Recommendations
For every missing skill, shows:

🆓 Free resource (YouTube, Kaggle, FreeCodeCamp)

💰 Paid course (Coursera, Udemy, etc.)

Helps users bridge the skill gap between their resume and job requirements.

📊 3. Analytics Dashboard
Built with Plotly for professional, interactive visuals.

Match Score Gauge: See your overall job readiness.

Bar Chart: Visual breakdown of matched vs. missing skills.

Color-coded alerts for instant clarity.

💎 4. Clean UI Enhancements
Better layout using Streamlit columns and progress indicators.

Skill results displayed using success, info, and error banners.

---

## 🗂️ Folder Structure

  smart_resume_analyzer/
  │
  ├── uploads/ # Uploaded resumes & JD files
  ├── app.py # Main Streamlit frontend
  ├── dashboard.py
  ├── feedback.py
  ├── jd_parser.py # JD skill extraction & filtering
  ├── matcher.py # Resume-JD skill matching logic
  ├── recommender.py # Skill → Course recommendations
  ├── requirements.txt # Project dependencies
  ├── resume_parser.py # PDF/DOCX text extraction
  ├── README.MD
  └── test_js.txt #testing exmple

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/smart_resume_analyzer.git
cd smart_resume_analyzer

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
🧩 Coming Soon
Phase	Features
Phase 5	📊 Career Analytics Dashboard
Phase 6	📤 PDF Export of Skill Gaps & Courses
Phase 7	🧠 LLM/GPT-based Job-Fit Explanation
Phase 8	🔎 Auto Web Scraping of Latest JD from Job Boards

👨‍💻 Author
Prakash L Waddar
AI Software Developer & Data Science Student

⭐ Give a Star
If you find this helpful, star the repo to show support! 🌟