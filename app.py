
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

@app.route('/addAdmin')
def addAdmin():
	return render_template('addAdmin.html')

@app.route('/addAppointment')
def addAppointment():
	return render_template('addAppointment.html')

@app.route('/addDonor')
def addDonor():
	return render_template('addDonor.html')

@app.route('/addFunds')
def addFunds():
	return render_template('addFunds.html')

@app.route('/addInventory')
def addInventory():
	return render_template('addInventory.html')

@app.route('/addSupplier')
def addSupplier():
	return render_template('addSupplier.html')

@app.route('/addVolunteer')
def addVolunteer():
	return render_template('addVolunteer.html')

@app.route('/editAdmin')
def editAdmin():
	return render_template('editAdmin.html')

@app.route('/editAppointment')
def editAppointment():
	return render_template('editAppointment.html')

@app.route('/editClient')
def editClient():
	return render_template('editClient.html')

@app.route('/editInventory')
def editInventory():
	return render_template('editInventory.html')

@app.route('/editVolunteer')
def editVolunteer():
	return render_template('editVolunteer.html')

@app.route('/viewAdmin')
def viewAdmin():
	return render_template('viewAdmin.html')

@app.route('/viewAppointment')
def viewAppointment():
	return render_template('viewAppointment.html')

@app.route('/viewClient')
def viewClient():
	return render_template('viewClient.html')

@app.route('/viewInventory')
def viewInventory():
	return render_template('viewInventory.html')

@app.route('/viewVolunteer')
def viewVolunteer():
	return render_template('viewVolunteer.html')


@app.route('/register', methods=['POST'])
def addClientUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# TODO: get the data from form
	# username = request.form['username']

	# TODO: put datat in
	c.execute(
		"INSERT INTO Account (username, email, accesslevel, password, userid) VALUES ('{name}', '{email}', {accesslevel}, '{password}', {userid})".format(
			name=request.form['username'],
			email=request.form['email'], accesslevel=1,
			password=request.form['password'],
			userid=request.form['userid']))
	
	conn.commit()
	conn.close()
	return redirect('/')

@app.route('/addNewAdmin', methods=['POST'])
def addAdminUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# TODO: get the data from form
	# username = request.form['username']

	# TODO: put datat in
	c.execute(
		"INSERT INTO Admin (id, name, phonenumber) VALUES ({id}, '{name}', '{phonenumber}')".format(
                        id=1,
			name=request.form['name'],
			phonenumber=request.form['phone']))

	c.execute(
		"INSERT INTO Account (username, email, accesslevel, password, userid) VALUES ('{username}', '{email}', {accesslevel}, '{password}', {userid})".format(
                        username=request.form['username'],
			email=request.form['email'],
			accesslevel=2,
                        password=request.form['password'],
                        userid=1))
	
	conn.commit()
	conn.close()
	return redirect('/admin')
