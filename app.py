
from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

currentUser = 0
currentId=0
#where 1 = client, 2 = user, 3 = admin





@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/admin')
def admin():
	global currentUser
	# if currentUser==3:
	# 	return render_template('admin.html')
	# else:
	# 	return render_template('index.html')

	return render_template('admin.html')


#############garbage

@app.route('/loginClient')
def loginClient():
	currentUser = 1
	return render_template('index.html')
	

###################

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/reqform')
def reqform():

	return render_template('reqform.html')

@app.route('/loginAccount', methods=['POST'])
def loginAccount():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# c.execute(
	# 	"INSERT INTO Client (name, email, username, password, income) VALUES ('{name}','{email}','{username}', '{password}', '{income}')".format(
	# 		name=request.form['name'],
	# 		email=request.form['email'],
	# 		username=request.form['username'],
	# 		password=request.form['password'],
	# 		income=request.form['income']))
	# t=(request.form['name'])
	# temp = (t,)
	# c.execute('SELECT * FROM Client WHERE name=?', temp)
	# key = c.fetchone()[0]


	if request.form['user'] == 'client':
		c.execute("SELECT * FROM Client")
		results = c.fetchall()
		print("checking clients")
		for x in results:
			if x[3] == request.form['username']:
				if x[4] == request.form['password']:
					currentUser = 1
					conn.commit()
					conn.close()
					print(currentUser)
					return redirect('/')


	elif request.form['user'] == 'volunteer':
		c.execute("SELECT * FROM Volunteer")
		results = c.fetchall()

		for x in results:
			if x[4] == request.form['username']:
				if x[5] == request.form['password']:
					currentUser = 2
					conn.commit()
					conn.close()
					print(currentUser)
					return redirect('/')


	elif request.form['user'] == 'admin':
		c.execute("SELECT * FROM Admin")
		results = c.fetchall()

		for x in results:
			if x[4] == request.form['username']:
				if x[5] == request.form['password']:
					currentUser = 3
					conn.commit()
					conn.close()
					print(currentUser)
					return redirect('/admin')

				

	conn.commit()
	conn.close()
	return redirect('/login')



@app.route('/addreqform', methods=['POST'])
def addreqform():
	error=None
	if(currentUser==1):

		conn = sqlite3.connect('foodbank.db')
		c = conn.cursor()

		t = (currentId)
		temp = (t,)
		famSize = c.execute("SELECT count(*) FROM Dependant WHERE id=?",temp)+1



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
				clientid=currentId))

		conn.commit()
		conn.close()
	else:
		error = "You must be logged in as a client to access this page"
	return render_template('index.html',error)

@app.route('/addAppointmentData', methods=['POST'])
def addAppointmentData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	volunteerExists = False
	clientExists=False
	t = (request.form['vID'])
	temp = (t,)
	for row in c.execute("SELECT * FROM Account WHERE id=?",temp):
		volunteerExists=True
		break
	else:
		print("volunteer not found")

	t = (request.form['cID'])
	temp = (t,)
	for row in c.execute("SELECT * FROM Account WHERE id=?",temp):
		clientExists=True
		break
	else:
		print("client not found")
	
	t = (request.form['time'])
	print(t+" this is time from form")
	#https://stackabuse.com/converting-strings-to-datetime-in-python/
	date_time_obj = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M')
	current = datetime.datetime.now()+datetime.timedelta(days=1)
	#print(current)
	#print(date_time_obj < current)
	#print("above is bool")

	#ensure that appointment times are at least 1 day away
	if (date_time_obj<current):
		if (volunteerExists and clientExists):
			c.execute(
				"INSERT INTO Appointment (time, clientid, volunteerid ) VALUES ('{time}', '{clientid}','{volunteerid}')".format(
					time=request.form['time'],
					clientid=request.form['cID'],
					volunteerid=request.form['vID']))
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

#client = 0, volunter = 1, admin = 2
#done
@app.route('/register', methods=['POST'])
def addClientUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()


	c.execute(
		"INSERT INTO Account (name, email, username, password, accounttype) VALUES ('{name}','{email}','{username}', '{password}', '{accounttype}')".format(
			name=request.form['name'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			accounttype=0))

	account_id = c.lastrowid
	c.execute(
		"INSERT INTO Client (income,accountid) VALUES ('{income}','{accountid}')".format(
			income=request.form['income'],
			accountid=account_id))

	#name=request.form['dname1']

	for _ in range(1,4):
		varname = 'dname'+str(_)
		relname = 'relation'+str(_)
		name=request.form[varname]
		if (name!=''):
			c.execute(
				"INSERT INTO Dependant (clientid,name,relationship) VALUES ('{clientid}','{name}','{relationship}')".format(
					clientid=account_id,
					name=request.form[varname],
					relationship=request.form[relname]))
		reasonname = 'reason'+str(_)
		reasonvar=request.form[reasonname]
		if (reasonvar!=''):
			c.execute(
				"INSERT INTO Reasons (clientid,reason) VALUES ('{clientid}','{reason}')".format(
					clientid=account_id,
					reason=request.form[reasonname]))
	
	conn.commit()
	conn.close()
	return redirect('/')

#done
@app.route('/addAdminUser', methods=['POST'])
def addAdminUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Account (name, email, username, password, accounttype) VALUES ('{name}','{email}','{username}', '{password}', '{accounttype}')".format(
			name=request.form['name'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			accounttype=2))
	account_id = c.lastrowid
	c.execute(
		"INSERT INTO Admin (phonenumber,accountid) VALUES ('{phonenumber}','{accountid}')".format(
			phonenumber=request.form['phone'],
			accountid=account_id))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

#done
@app.route('/addVolunteerUser', methods=['POST'])
def addVolunteerUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	
	t = (request.form['mID'])
	temp = (t,)
	#https://stackoverflow.com/questions/30041983/check-if-a-row-exists-in-sqlite3?rq=1
	for row in c.execute("SELECT * FROM Account WHERE id=?",temp):
		c.execute(
			"INSERT INTO Account (name, email, username, password, accounttype) VALUES ('{name}','{email}','{username}', '{password}', '{accounttype}')".format(
				name=request.form['name'],
				email=request.form['email'],
				username=request.form['username'],
				password=request.form['password'],
				accounttype=1))
		account_id = c.lastrowid
		c.execute(
			"INSERT INTO Volunteer (phonenumber,availability,accountid,managerid) VALUES ('{phonenumber}','{availability}','{accountid}','{managerid}')".format(
				phonenumber=request.form['phone'],
				availability=request.form['availability'],
				accountid=account_id,
				managerid=request.form['mID']))
		break
	else:
		print("not found")


	# c.execute(
	# 	"INSERT INTO Account (name, email, username, password, accounttype) VALUES ('{name}','{email}','{username}', '{password}', '{accounttype}')".format(
	# 		name=request.form['name'],
	# 		email=request.form['email'],
	# 		username=request.form['username'],
	# 		password=request.form['password'],
	# 		accounttype=1))
	# account_id = c.lastrowid
	# c.execute(
	# 	"INSERT INTO Volunteer (phonenumber,availability,accountid,managerid) VALUES ('{phonenumber}','{availability}','{accountid}','{managerid}')".format(
	# 		phonenumber=request.form['phone'],
	# 		availability=request.form['availability'],
	# 		accountid=account_id,
	# 		managerid=request.form['mID']))
	
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

#done
@app.route('/addDonorData')
def addDonorData():

	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Donor (name,phonenumber,email) VALUES ('{name}','{phonenumber}','{email}')".format(
			name=request.form['name'],
			phonenumber=request.form['phonenumber'],
			email=request.form['email']))
	
	conn.commit()
	conn.close()


	return redirect('/admin')

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

#done but add page
@app.route('/addFoodBankData')
def addFoodBankData():

	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Foodbank (address,phonenumber,email,hours,funds) VALUES ('{address}','{phonenumber}','{email}', '{hours}', '{funds}')".format(
			address=request.form['address'],
			phonenumber=request.form['phonenumber'],
			email=request.form['email'],
			hours=request.form['funds']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

@app.route('/addFoodBank')
def addFoodBank():
	return render_template('addFoodBank.html')

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

	c.execute("SELECT * FROM Account INNER JOIN Admin ON Account.id=Admin.accountid")

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

#done
@app.route('/viewClient')
def viewClient():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Account INNER JOIN Client ON Account.id=Client.accountid")
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

@app.route('/viewOrder')
def viewOrder():
	#if currentUser==2 or currentUser==3:

	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM RequestForm")
	results = c.fetchall()
	print(results)

	return render_template('viewOrder.html', data=results)
	#else:
	#	return redirect('/')


@app.route('/deleteAdminUser',methods=['POST'])
def deleteAdminUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Admin WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewAdmin')


@app.route('/deleteVolunteerUser',methods=['POST'])
def deleteVolunteerUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Volunteer WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewVolunteer')

@app.route('/deleteClientUser',methods=['POST'])
def deleteClientUser():
	conn = sqlite3.connect('foodbank.db')
	conn.execute("PRAGMA foreign_keys = ON")
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Account WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewClient')

@app.route('/deleteOrderData',methods=['POST'])
def deleteOrderData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM RequestForm WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewOrder')

@app.route('/deleteAppointmentData',methods=['POST'])
def deleteAppointmentData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Appointment WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewAppointment')

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


@app.route('/finishOrder')
def finishOrder():




	return redirect('/')

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


