import spacy

nlp = spacy.load("en_core_web_sm")


def extract_skills_from_jd(jd_text):
    doc = nlp(jd_text)
    raw_keywords = set()

    for chunk in doc.noun_chunks:
        text = chunk.text.strip().lower()
        if (
            len(text) > 2
            and not text.startswith("*")
            and not text.startswith("-")
            and not text.startswith("**")
            and "responsibilities" not in text
            and "degree" not in text
        ):
            raw_keywords.add(text)

    return sorted(list(raw_keywords))

KNOWN_TECH_SKILLS = [
    "python", "sql", "tableau", "power bi", "matplotlib",
    "excel", "statistics", "machine learning", "data visualization",
    "data analysis", "dashboard", "pandas", "numpy", "seaborn"
]

def filter_tech_skills(keywords):
    filtered = []

    for kw in keywords:
        for tech in KNOWN_TECH_SKILLS:
            if tech in kw:
                filtered.append(tech)
                break
    
    return sorted(list(filtered))