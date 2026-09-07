# Week 1 — Shared Chore Manager

## Scope decisions
- Multi-member household
- Manual chore assignment
- Approval needed for completion
- Points / leaderboard

## What's built
- Django project `chores_project` with app `chores`
- Models: Household, Roommate, Chore
- Views: list, create, toggle-done
- Minimal HTML/CSS UI

## How to run
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/
