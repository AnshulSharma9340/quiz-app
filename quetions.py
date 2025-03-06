from app import create_app, db
from app.models import Questions
app = create_app()

with app.app_context():
    q1 = Questions(
        ques = "Which among the following is not a Laptop brand?",
        a = "HP",
        b = "Dell",
        c = "Tesla",
        d = "Toshiba",
        ans ="Tesla" 
    )
    q2 = Questions(
        ques = "Odumeje have All the following powers except?",
        a = "Abido Shaker",
        b = "Gandusa Ganduja",
        c = "Indaboski Bahose",
        d = "Kadosh Kadosh",
        ans ="Kadosh Kadosh" 
    )
    q3 = Questions(
        ques="What is the primary language used for Android app development?",
        a="Swift",
        b="Java",
        c="C#",
        d="Ruby",
        ans="Java"
    )
    q4 = Questions(
        ques="Which technology is used to make telephone calls over the Internet possible?",
        a="VoIP",
        b="SMTP",
        c="HTTP",
        d="FTP",
        ans="VoIP"
    )
    q5 = Questions(
    ques="Which African city is home to the first ALX campus?",
    a="Nairobi",
    b="Johannesburg",
    c="Lagos",
    d="Addis Ababa",
    ans="Nairobi"
    )


    db.session.add_all([q1,q2,q3,q4,q5])
    db.session.commit()