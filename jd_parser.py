import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# 1. Extract all noun phrases from JD/resume text
def extract_skills_from_jd(jd_text):
    doc = nlp(jd_text)
    raw_keywords = set()

    for chunk in doc.noun_chunks:
        text = chunk.text.strip().lower()
        if (
            len(text) > 2
            and not text.startswith(("*", "-", "**"))  # cleaner
            and "responsibilities" not in text
            and "degree" not in text
        ):
            raw_keywords.add(text)

    return sorted(raw_keywords)


# 2. Match keywords to known technical skills
KNOWN_TECH_SKILLS = [
    "python", "sql", "tableau", "power bi", "matplotlib",
    "excel", "statistics", "machine learning", "data visualization",
    "data analysis", "dashboard", "pandas", "numpy", "seaborn",
    "scikit-learn", "deep learning", "tensorflow", "keras",
    "flask", "django", "nlp", "computer vision", "big data"
]

def filter_tech_skills(keywords):
    filtered = []
    for kw in keywords:
        for tech in KNOWN_TECH_SKILLS:
            # Match exact tech word or close phrase (e.g., "python skills")
            if tech in kw:
                filtered.append(tech)
                break
    return sorted(set(filtered))
