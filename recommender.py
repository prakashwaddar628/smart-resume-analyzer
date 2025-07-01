COURSE_RECOMMENDATIONS = {
    "python": {
        "free": "https://www.freecodecamp.org/learn/scientific-computing-with-python/",
        "paid": "https://www.coursera.org/learn/python"
    },
    "sql": {
        "free": "https://www.kaggle.com/learn/intro-to-sql",
        "paid": "https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/"
    },
    "power bi": {
        "free": "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "paid": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"
    },
    "machine learning": {
        "free": "https://www.kaggle.com/learn/intro-to-machine-learning",
        "paid": "https://www.coursera.org/learn/machine-learning"
    },
    "tableau": {
        "free": "https://www.youtube.com/playlist?list=PLUaB-1hjhk8H48Pj32z4GZgGWyylqv85f",
        "paid": "https://www.tableau.com/learn/training/20221"
    },
    "excel": {
        "free": "https://www.youtube.com/watch?v=Iim3B5HRd3o",
        "paid": "https://www.coursera.org/learn/excel-data-analysis"
    },
    "numpy": {
        "free": "https://www.kaggle.com/learn/numpy",
        "paid": "https://www.udemy.com/course/data-science-and-machine-learning-with-python/"
    },
    "pandas": {
        "free": "https://www.kaggle.com/learn/pandas",
        "paid": "https://www.udemy.com/course/data-manipulation-with-pandas-python/"
    },
    "matplotlib": {
        "free": "https://www.youtube.com/watch?v=3Xc3CA655Y4",
        "paid": "https://www.udemy.com/course/python-for-data-visualization/"
    },
    "seaborn": {
        "free": "https://www.kaggle.com/learn/data-visualization",
        "paid": "https://www.udemy.com/course/python-for-data-visualization/"
    },
    "scikit-learn": {
        "free": "https://www.youtube.com/watch?v=0Lt9w-BxKFQ",
        "paid": "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/"
    },
    "tensorflow": {
        "free": "https://www.tensorflow.org/tutorials",
        "paid": "https://www.coursera.org/learn/introduction-tensorflow"
    },
    "keras": {
        "free": "https://keras.io/getting_started/",
        "paid": "https://www.udemy.com/course/deep-learning-keras-tensorflow/"
    },
    "nlp": {
        "free": "https://www.kaggle.com/learn/natural-language-processing",
        "paid": "https://www.coursera.org/learn/language-processing"
    },
    "flask": {
        "free": "https://www.youtube.com/watch?v=Z1RJmh_OqeA",
        "paid": "https://www.coursera.org/projects/python-flask"
    },
    "django": {
        "free": "https://www.youtube.com/watch?v=F5mRW0jo-U4",
        "paid": "https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/"
    },
    "git": {
        "free": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "paid": "https://www.udemy.com/course/git-and-github-bootcamp/"
    },
    "linux": {
        "free": "https://ubuntu.com/tutorials/command-line-for-beginners",
        "paid": "https://www.udemy.com/course/linux-command-line-tutorial/"
    },
    "data structures": {
        "free": "https://www.geeksforgeeks.org/data-structures/",
        "paid": "https://www.coursera.org/specializations/data-structures-algorithms"
    },
    "algorithms": {
        "free": "https://visualgo.net/en",
        "paid": "https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/"
    }
}



def get_course_links(missing_skills):
    results = {}
    for skill in missing_skills:
        if skill in COURSE_RECOMMENDATIONS:
            results[skill] = COURSE_RECOMMENDATIONS[skill]
    return results
