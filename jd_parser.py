import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Known tech skills to match against
KNOWN_TECH_SKILLS = [
    "python", "sql", "tableau", "power bi", "matplotlib",
    "excel", "statistics", "machine learning", "data visualization",
    "data analysis", "dashboard", "pandas", "numpy", "seaborn",
    "scikit-learn", "deep learning", "tensorflow", "keras",
    "flask", "django", "nlp", "computer vision", "big data",
    "mongodb", "hadoop", "spark", "git", "github", "linux"
]

# 1. Extract possible skill-related phrases using spaCy + fallback parsing
def extract_skills_from_jd(text):
    doc = nlp(text)
    raw_keywords = set()

    # Add noun chunks (phrases like "data analysis")
    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip().lower()
        if (
            len(phrase) > 2
            and not phrase.startswith(("*", "-", "**"))
            and "responsibilities" not in phrase
            and "degree" not in phrase
        ):
            raw_keywords.add(phrase)

    # Add noun and proper nouns from tokens (e.g., 'python', 'sql')
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and not token.is_punct:
            raw_keywords.add(token.text.strip().lower())

    # Optional: Extract after keywords like "Skills:", "Technologies:"
    pattern_skills = re.findall(r"skills[:\-]*([\s\S]+?)(?:experience|projects|education|$)", text.lower())
    for match in pattern_skills:
        lines = re.split(r"[\n,•\-]", match)
        for item in lines:
            item = item.strip().lower()
            if 2 < len(item) < 40:
                raw_keywords.add(item)

    return sorted(raw_keywords)


# 2. Match extracted keywords to known tech skills
def filter_tech_skills(keywords):
    print("Incoming keywords:", keywords)
    filtered = []

    for kw in keywords:
        for tech in KNOWN_TECH_SKILLS:
            if tech in kw:  # using lowercase already
                filtered.append(tech)
                break

    print("Filtered skills:", filtered)
    return sorted(set(filtered))
