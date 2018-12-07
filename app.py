
from flask import Flask, render_template, request, redirect
import sqlite3
import random as rnd

app = Flask(__name__)

currentUser = 0
#where 1 = client, 2 = user, 3 = admin

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/admin')
def admin():
	# global currentUser
	# if currentUser==3:
		return render_template('admin.html')
	# else:
	# 	return render_template('index.html')

#############garbage

@app.route('/loginClient')
def loginClient():
	currentUser = 1
	return render_template('index.html')
	

####################

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/reqform')
def reqform():
	return render_template('reqform.html')

@app.route('/loginAccount')
def loginAccount():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()


	if request.form['user'] == 'client':
				c.execute("SELECT * FROM Client")
				results = c.fetchall()

				for x in results:
						if x[3] == request.form['username']:
								if x[4] == request.form['password']:
										currentUser = 1
										conn.commit()
										conn.close()
										return redirect('/')


	elif request.form['user'] == 'volunteer':
				c.execute("SELECT * FROM Volunteer WHERE username=?")
				results = c.fetchone()[0]

				for x in results:
						if x[4] == request.form['username']:
								if x[5] == request.form['password']:
										currentUser = 2
										conn.commit()
										conn.close()
										return redirect('/')


	elif request.form['user'] == 'admin':
				c.execute("SELECT * FROM Admin WHERE username=?")
				results = c.fetchone()[0]

				for x in results:
						if x[4] == request.form['username']:
								if x[5] == request.form['password']:
										currentUser = 3
										conn.commit()
										conn.close()
										return redirect('/admin')

				

	conn.commit()
	conn.close()
	return redirect('/login')



@app.route('/addreqform', methods=['POST'])
def addreqform():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	c.execute(
		"INSERT INTO RequestForm (fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat, clientid, date) VALUES ('{fruits}','{vegetables}','{potatoBags}', '{eggs}','{butter}', '{groundBeef}', '{wholeChicken}', '{veggieFrozen}', '{bread}', '{cannedVeggie}', '{cannedFruit}', '{cannedSoup}', '{cannedSeafood}', '{cannedMeat}', '{clientid}', '{date}' )".format(
			fruits=request.form['freshfruit'],
			vegetables=request.form['carrot'],
			potatoBags=request.form['potato'],
			eggs=request.form['eggs'],
			butter=request.form['butt'],
			groundBeef=request.form['beef'],
			wholeChicken=request.form['chicken'],
			veggieFrozen=request.form['frovege'],
			bread=request.form['bread'],
			cannedVeggie=request.form['vege'],
			cannedFruit=request.form['fruit'],
			cannedSoup=request.form['soup'],
			cannedSeafood=request.form['cseafood'],
			cannedMeat=request.form['cmeat'],
			clientid=request.form['id'],
			date=request.form['pickupdate']))

	conn.commit()
	conn.close()
	return redirect('/')

@app.route('/addAppointmentData', methods=['POST'])
def addAppointmentData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	c.execute(
		"INSERT INTO Admin (name, phonenumber, email, username, password) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password']))
	conn.commit()
	conn.close()
	return redirect('/')

@app.route('/addInventoryData', methods=['POST'])
def addInventoryData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	c.execute(
		"INSERT INTO Foodstore (fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat) VALUES ('{fruits}','{vegetables}','{potatoBags}', '{eggs}','{butter}', '{groundBeef}', '{wholeChicken}', '{veggieFrozen}', '{bread}', '{cannedVeggie}', '{cannedFruit}', '{cannedSoup}', '{cannedSeafood}', '{cannedMeat}' )".format(
			fruits=request.form['freshfruit'],
			vegetables=request.form['carrot'],
			potatoBags=request.form['potato'],
			eggs=request.form['eggs'],
			butter=request.form['butt'],
			groundBeef=request.form['beef'],
			wholeChicken=request.form['chicken'],
			veggieFrozen=request.form['frovege'],
			bread=request.form['bread'],
			cannedVeggie=request.form['vege'],
			cannedFruit=request.form['fruit'],
			cannedSoup=request.form['soup'],
			cannedSeafood=request.form['cseafood'],
			cannedMeat=request.form['cmeat']))

	conn.commit()
	conn.close()
	return redirect('/')


@app.route('/register', methods=['POST'])
def addClientUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Client (name, email, username, password, income) VALUES ('{name}','{email}','{username}', '{password}', '{income}')".format(
			name=request.form['name'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			income=request.form['income']))
	t=(request.form['name'])
	temp = (t,)
	c.execute('SELECT * FROM Client WHERE name=?', temp)
	key = c.fetchone()[0]

	#need to do this for all dependents?  how to for loop lmao
	c.execute(
		"INSERT INTO Dependant (clientid,name,relationship) VALUES ('{clientid}','{name}','{relationship}')".format(
			clientid=key,
			name=request.form['dname1'],
			relationship=request.form['relation1']))
	
	conn.commit()
	conn.close()
	return redirect('/')

@app.route('/addAdminUser', methods=['POST'])
def addAdminUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# TODO: get the data from form
	# username = request.form['username']

	# TODO: put datat in
	c.execute(
		"INSERT INTO Admin (name, phonenumber, email, username, password) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

@app.route('/addVolunteerUser', methods=['POST'])
def addVolunteerUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Volunteer (name, phonenumber, email,  username, password, availability) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}','{availability}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			availability=request.form['availability']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

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


@app.route('/editAdminUser', methods=['POST'])
def editAdminUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	newName = ""
	newPhone = ""

	c.execute("SELECT * FROM Admin WHERE id=?", (request.form['id']))
	results = c.fetchone()
	if results is not None:
                if request.form['name'] != "":
                        newName = request.form['name']
                else:
                        c.execute("SELECT name FROM Admin WHERE id=?", (request.form['id']))
                        newName = c.fetchone()[0]
                        
                if request.form['phone'] != "":
                        newPhone = request.form['phone']
                else:
                        c.execute("SELECT phonenumber FROM Admin WHERE id=?", (request.form['id']))
                        newPhone = c.fetchone()[0]

        


	c.execute(
		"INSERT INTO Admin (name, phonenumber, email, username, password) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

@app.route('/viewAdmin')
def viewAdmin():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Admin")
	results = c.fetchall()
	print(results)

	return render_template('viewAdmin.html', data=results)
	

@app.route('/viewVolunteer')
def viewVolunteer():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Volunteer")
	results = c.fetchall()
	print(results)
	return render_template('viewVolunteer.html', data=results)

@app.route('/viewClient')
def viewClient():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Client")
	results = c.fetchall()
	print(results)
	return render_template('viewClient.html', data=results)

@app.route('/viewAppointment')
def viewAppointment():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Appointment")
	results = c.fetchall()
	print(results)
	return render_template('viewAppointment.html', data=results)

@app.route('/viewInventory')
def viewInventory():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Foodstore")
	results = c.fetchall()
	print(results)

	return render_template('viewInventory.html', data=results)

@app.route('/deleteAdmin')
def deleteAdmin():
	return render_template('deleteAdmin.html')

@app.route('/deleteVolunteer')
def deleteVolunteer():
	return render_template('deleteVolunteer.html')

@app.route('/deleteClient')
def deleteClient():
	return render_template('deleteClient.html')

@app.route('/deleteOrder')
def deleteOrder():
	return render_template('deleteOrder.html')

@app.route('/deleteAppointment')
def deleteAppointment():
	return render_template('deleteAppointment.html')

@app.route('/deleteInventory')
def deleteInventory():
	return render_template('deleteInventory.html')

@app.route('/deleteAdminUser')
def deleteAdminUser():
	return render_template('editAdmin.html')

# @app.route('/editAdmin')
# def editAdmin():
# 	return render_template('editAdmin.html')

# @app.route('/editAppointment')
# def editAppointment():
# 	return render_template('editAppointment.html')

# @app.route('/editClient')
# def editClient():
# 	return render_template('editClient.html')

# @app.route('/editInventory')
# def editInventory():
# 	return render_template('editInventory.html')

# @app.route('/editVolunteer')
# def editVolunteer():
# 	return render_template('editVolunteer.html')


