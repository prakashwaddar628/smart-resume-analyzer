COURSE_RECOMMENDATIONS = {
    "python": "https://www.coursera.org/learn/python",
    "sql": "https://www.kaggle.com/learn/intro-to-sql",
    "power bi": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "tableau": "https://www.tableau.com/learn/training/20221",
    # Add more
}

def get_course_links(missing_skills):
    return {skill: COURSE_RECOMMENDATIONS.get(skill) for skill in missing_skills if skill in COURSE_RECOMMENDATIONS}