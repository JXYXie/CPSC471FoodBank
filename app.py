
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/reqform')
def reqform():
	return render_template('reqform.html')

@app.route('/register', methods=['POST'])
def addUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# TODO: get the data from form
	# username = request.form['username']

	# TODO: put datat in
	c.execute(
		"INSERT INTO Account (username, email, accesslevel, password, userid) VALUES ('{name}', '{email}', {accesslevel}, '{password}', '{userid}')".format(
			name=request.form['username'],
			email=request.form['email'], accesslevel=1,
			password=request.form['password'],
			userid=request.form['userid']))
	
	conn.commit()
	conn.close()
	return redirect('/')
