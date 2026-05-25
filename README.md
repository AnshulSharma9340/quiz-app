# Quiz App

A simple multiple-choice quiz web application built with Flask. Users can register, log in, take a timed quiz, and view their score history on a personal profile page.

This is my first full-stack project — built end to end and deployed to the public web.

## Features

- User registration and login (password hashing with Werkzeug)
- Session-based authentication using Flask-Login
- Timed quiz (5 minutes) with multiple-choice questions
- 10 points per correct answer
- Score history saved per user
- Auto-seeds a default question bank on first run
- Deployable to Render with one click

## Tech Stack

- **Backend:** Flask 3, Flask-SQLAlchemy, Flask-Login, Flask-WTF
- **Database:** SQLite (local) / PostgreSQL (production via `DATABASE_URL`)
- **Frontend:** Bootstrap 4, Jinja2 templates
- **Server:** Gunicorn

## Project Structure

```
quiz-app/
├── app/
│   ├── __init__.py        # App factory, DB + login setup, auto-seed
│   ├── auth.py            # Login / register / logout / profile
│   ├── route.py           # Index, instructions, questions, score
│   ├── models.py          # User, Questions, Score models
│   ├── forms.py           # WTForms for auth & quiz
│   ├── seed.py            # Default question bank
│   ├── static/            # CSS and images
│   └── templates/         # Jinja2 templates
├── config.py              # Reads SECRET_KEY and DATABASE_URL from env
├── run.py                 # Entry point
├── requirements.txt
├── Procfile               # gunicorn run:app
├── render.yaml            # Render blueprint
└── runtime.txt            # Python version pin
```

## Run Locally

```bash
git clone https://github.com/AnshulSharma9340/quiz-app.git
cd quiz-app

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python run.py
```

Open http://localhost:8000 in your browser. The database and default questions are created automatically on first run.

## Environment Variables

| Variable       | Required? | Default                   | Notes                                                      |
| -------------- | --------- | ------------------------- | ---------------------------------------------------------- |
| `SECRET_KEY`   | Yes (prod)| `dev-secret-change-me`    | Used to sign session cookies. Set a strong random value.   |
| `DATABASE_URL` | No        | `sqlite:///quiz.db`       | Standard SQLAlchemy URL. `postgres://` is auto-normalized. |
| `PORT`         | No        | `8000`                    | Used only by `python run.py`; gunicorn sets its own.       |

## Deploy to Render

The repo includes a `render.yaml` blueprint, so deployment is two clicks:

1. Push this repo to GitHub.
2. Go to https://dashboard.render.com → **New** → **Blueprint** → connect this repo.
3. Render will read `render.yaml`, install dependencies, set `SECRET_KEY` automatically, and start the app with gunicorn.

Manual setup (without the blueprint):

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn run:app`
- **Environment:** add `SECRET_KEY` (any long random string)

## Author

**Anshul Sharma** — [@AnshulSharma9340](https://github.com/AnshulSharma9340)

## License

MIT
