def match_skills(resume_skills, jd_skills):
    resume_set = set([skill.lower() for skill in resume_skills])
    jd_set = set([skill.lower() for skill in jd_skills])

    matched = resume_set.intersection(jd_set)
    missing = jd_set.difference(resume_set)

    match_score = (len(matched) / len(jd_set)) * 100 if jd_set else 0

    return {
        "matched_skills" : sorted(matched),
        "missing_skills" : sorted(missing),
        "match_score" : round(match_score, 2)
    }