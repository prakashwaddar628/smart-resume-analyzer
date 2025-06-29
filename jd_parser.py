import spacy

nlp = spacy.load("en_core_web_sm")


def extract_skills_from_jd(jd_text):
    doc = nlp(jd_text)
    keywords = set()

    for chunk in doc.noun_chunks:
        if len(chunk.text) > 2:
            keywords.add(chunk.text.strip().lower())

    return sorted(list(keywords))