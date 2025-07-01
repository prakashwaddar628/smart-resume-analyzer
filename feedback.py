def generate_feedback(missing_skills):
    if not missing_skills:
        return "🎉 Your resume already covers all required skills for this job. Great work!"
    
    feedback = "Here are some suggestions to improve your resume based on missing skills:\n\n"

    for skill in missing_skills:
        feedback += "f• Learn or highlight your experience with **{skill.title()}**.\n"
    return feedback