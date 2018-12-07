sqlite3 foodbank.db < foodbank.sql

export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
