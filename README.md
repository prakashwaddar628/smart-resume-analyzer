# 🧠 Smart Resume Analyzer

An AI-powered tool that analyzes your resume against job descriptions and provides personalized feedback, missing skills, and upskilling course recommendations. Built using **Streamlit**, **spaCy**, **Plotly**, and custom NLP logic.

---

## 📌 Project Overview

The **Smart Resume Analyzer** helps students and professionals boost their job readiness by:

- Extracting skill-related content from resumes
- Comparing it with a job description (JD)
- Highlighting skill gaps
- Recommending curated **free & paid courses** to fill the gaps
- Providing AI-powered resume feedback and dashboards

---

## 🛠️ Tech Stack

| Layer        | Technology                         |
|--------------|-------------------------------------|
| UI           | Streamlit                           |
| NLP Engine   | spaCy                               |
| Text Parsing | pdfminer.six, python-docx           |
| Matching     | Custom logic (set-based comparison) |
| Dashboard    | Plotly                              |
| Upskilling   | Kaggle, YouTube, Coursera, Udemy    |

---

## 🚀 Feature Progression (Phases)

### ✅ Phase 1: Resume Upload & Text Extraction
- Upload resume in `.pdf` or `.docx`
- Extracts and displays text cleanly using `pdfminer` and `docx2txt`

### ✅ Phase 2: JD Upload/Input & Skill Extraction
- JD input via text box or upload
- Extracts technical skills using spaCy noun phrases
- Filters only known technical keywords

### ✅ Phase 3: Resume vs JD Skill Matching
- Compares extracted skills
- Calculates **match score**
- Highlights:
  - ✅ Matching Skills
  - ❌ Missing Skills

### ✅ Phase 4: GPT Feedback + Skill Recommendations
- **Smart Feedback** for missing skills using GPT-like logic
- **Free & Paid Courses** shown for each missing skill
  - Platforms: Kaggle, Coursera, YouTube, Udemy, FreeCodeCamp

### ✅ Phase 5: Analytics Dashboard
- **Match Score Gauge** (Plotly)
- **Skill Bar Chart**: Matched vs Missing
- Professional UI using Streamlit columns, themes & layout
- Copyright

---

## 📊 Sample Output

**Job Description:** Data Analyst @ Flipkart  
**Match Score:** `68%`

- ✅ Matching Skills:
  - Python, SQL, Excel
- ❌ Missing Skills:
  - Tableau, Power BI, Machine Learning

**🎓 Recommended Courses:**

- **Tableau**
  - 🆓 [Free Course](https://www.youtube.com/playlist?list=PLUaB-1hjhk8H48Pj32z4GZgGWyylqv85f)
  - 💰 [Paid Course](https://www.tableau.com/learn/training/20221)

- **Machine Learning**
  - 🆓 [Free Course](https://www.kaggle.com/learn/intro-to-machine-learning)
  - 💰 [Paid Course](https://www.coursera.org/learn/machine-learning)

---

## 📁 Folder Structure
    smart_resume_analyzer/
    │
    ├── uploads/ # Uploaded resumes & JD files
    ├── app.py # Main Streamlit frontend
    ├── dashboard.py # Analytics Dashboard with Plotly
    ├── feedback.py # GPT-like skill feedback generator
    ├── jd_parser.py # JD skill extraction & filtering
    ├── matcher.py # Resume-JD skill matching logic
    ├── recommender.py # Skill → Course recommendations
    ├── requirements.txt # Project dependencies
    ├── resume_parser.py # PDF/DOCX text extraction
    ├── README.MD # You're reading this :)
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
Phase 6	📤 PDF Export of Skill Gaps
Phase 7	🧠 LLM-based Job Fit Justification (GPT)
Phase 8	🔎 Auto Job Scraper (LinkedIn, Naukri, etc.)

👨‍💻 Author
Prakash L Waddar
AI Software Developer & Data Science Student

⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub!
Together, let’s make resumes smarter. 🚀