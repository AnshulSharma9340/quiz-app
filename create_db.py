from app import create_app, db

def create_database():
    app = create_app()
    print(app)
    with app.app_context():
        result = db.create_all()
        print(result)
        #     print("Database tables created.")
        # else:
        #     print("Fail to create db")

if __name__ == '__main__':
    create_database()
