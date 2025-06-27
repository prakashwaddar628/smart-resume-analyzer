# 🧠 Smart Resume Analyzer - Phase 1

A Streamlit-based application that lets users upload their resume (`.pdf` or `.docx`) and extracts the raw text using NLP libraries. This is **Phase 1** of a full AI + Data Science project aimed at **smart resume-job matching and personalized career recommendations**.

---

## 🚀 Features (Phase 1)

- Upload resume in PDF or Word format
- Automatically extract clean text from resume
- View the extracted resume content in the UI
- Save the text for future AI-based processing

---

## 📂 Project Structure

smart_resume_analyzer/
├── app.py # Streamlit frontend
├── resume_parser.py # Resume parsing logic (PDF/DOCX)
├── uploads/ # Folder to store uploaded files
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ How to Run

### 1. Clone the repo:
```bash
git clone https://github.com/<your-username>/smart_resume_analyzer.git
cd smart_resume_analyzer

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:
```bash
pip install -r requirements.txt

4. Run the Streamlit app:
```bash
streamlit run app.py

✅ Next Phases
Phase	Description
Phase 2	Parse job descriptions & extract skill requirements
Phase 3	Match resume vs JD using NLP models
Phase 4	Generate feedback using GPT/LLM
Phase 5	Recommend skills, certifications, and courses
Phase 6	Add analytics dashboard & job scraper integration


📌 Author
Prakash L Waddar
AI Software Developer & Data Science Enthusiast