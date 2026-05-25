from app import db
from app.models import Questions

DEFAULT_QUESTIONS = [
    {
        "ques": "Which among the following is not a Laptop brand?",
        "a": "HP", "b": "Dell", "c": "Tesla", "d": "Toshiba",
        "ans": "Tesla",
    },
    {
        "ques": "What is the primary language used for Android app development?",
        "a": "Swift", "b": "Java", "c": "C#", "d": "Ruby",
        "ans": "Java",
    },
    {
        "ques": "Which technology is used to make telephone calls over the Internet possible?",
        "a": "VoIP", "b": "SMTP", "c": "HTTP", "d": "FTP",
        "ans": "VoIP",
    },
    {
        "ques": "Which language runs in a web browser?",
        "a": "Java", "b": "C", "c": "Python", "d": "JavaScript",
        "ans": "JavaScript",
    },
    {
        "ques": "What does CSS stand for?",
        "a": "Central Style Sheets",
        "b": "Cascading Style Sheets",
        "c": "Cascading Simple Sheets",
        "d": "Cars SUVs Sailboats",
        "ans": "Cascading Style Sheets",
    },
    {
        "ques": "What does HTML stand for?",
        "a": "Hypertext Markup Language",
        "b": "Hypertext Markdown Language",
        "c": "Hyperloop Machine Language",
        "d": "Helicopters Terminals Motorboats Lamborginis",
        "ans": "Hypertext Markup Language",
    },
    {
        "ques": "What year was JavaScript launched?",
        "a": "1996", "b": "1995", "c": "1994", "d": "none of the above",
        "ans": "1995",
    },
]


def seed_questions():
    if Questions.query.first():
        return
    for q in DEFAULT_QUESTIONS:
        db.session.add(Questions(**q))
    db.session.commit()
