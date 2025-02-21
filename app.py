
from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

currentUser = -1
currentId=-1

#client = 0, volunter = 1, admin = 2 for accounttype field


@app.route('/')
def hello_world():
	global currentUser
	global currentId
	print("currentUser is "+str(currentUser))
	print("currentId is "+str(currentId))
	return render_template('index.html')

@app.route('/admin')
def admin():
	global currentUser
	global currentId
	print("currentUser is "+str(currentUser))
	print("currentId is "+str(currentId))
	if currentUser>0:
		return render_template('admin.html')
	else:
		return render_template('index.html')


@app.route('/login')
def login():
	global currentUser
	global currentId

	if (currentUser==-1):
		return render_template('login.html')
	else:
		currentUser=-1
		currentId=-1
		return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/reqform')
def reqform():
	global currentUser

	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM MaxRequests")
	results = c.fetchall()

	global currentUser
	print(currentUser)
	if (currentUser>-1):
		return render_template('reqform.html',data=results)
	else:
		return render_template('index.html')


@app.route('/loginAccount', methods=['POST'])
def loginAccount():
	global currentUser
	global currentId
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	error=None


	# if request.form['user'] == 'client':
	# 	c.execute("SELECT * FROM Client")
	# 	results = c.fetchall()
	# 	print("checking clients")
	# 	for x in results:
	# 		if x[0] == request.form['username']:
	# 			if x[4] == request.form['password']:
	# 				currentUser = 1
	# 				conn.commit()
	# 				conn.close()
	# 				print(currentUser)
	# 				return redirect('/')

#client = 0, volunter = 1, admin = 2 for accounttype field
#1 = client, 2 = user, 3 = admin for currentuser

	c.execute("SELECT * FROM Account")
	results = c.fetchall()
	for x in results:
		print(x[3])
		print(x[4])
		print(x[5])
		if x[3] == request.form['username']:
			print("user matched")
			if x[4] == request.form['password']:
				print("password matched")
				print(request.form['user'])
				print(x[5])
				print("above is accounttype")
				temp = int(request.form['user'])
				if (x[5] == temp):
					currentUser=temp
					currentId=x[0]
	conn.commit()
	conn.close()
	print(currentUser)

	if (currentUser==-1):
		return redirect('/login')
	elif (currentUser==2):
		return redirect('/admin')
	else:
		return redirect('/')

@app.route('/addreqform', methods=['POST'])
def addreqform():
	error=None
	global currentId
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	t = (currentId)
	temp = (t,)
	cursor = c.execute("SELECT * FROM Dependant WHERE clientid=?",temp)
	famSize = len(cursor.fetchall()) + 1
	print(famSize)

	t = (famSize)
	temp = (t,)
	print(temp)
	cursor = c.execute("SELECT * FROM MaxRequests WHERE famSize=?",temp)
	max = cursor.fetchone()
	print(max)
	max = list(max)
	max.pop(0)

	a=[]
	a.append(request.form['freshfruit']),
	a.append(request.form['carrot']),
	a.append(request.form['potato']),
	a.append(request.form['eggs']),
	a.append(request.form['butt']),
	a.append(request.form['beef']),
	a.append(request.form['chicken']),
	a.append(request.form['frovege']),
	a.append(request.form['bread']),
	a.append(request.form['vege']),
	a.append(request.form['fruit']),
	a.append(request.form['soup']),
	a.append(request.form['cseafood']),
	a.append(request.form['cmeat']),		
	a=list(map(int,a))
	print(a)
	allSmaller = True
	print(max)
	for _ in range(len(max)):
		if (a[_]>max[_]):
			allSmaller = False
			break
	print(allSmaller)
	t = (request.form['date'])
	date_time_obj = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M')
	current = datetime.datetime.now()+datetime.timedelta(days=1)

	c.execute("SELECT * FROM MaxRequests")
	results = c.fetchall()

	if (date_time_obj>current):
		print("OuterIf")
		if (allSmaller):
			c.execute(
				"INSERT INTO RequestForm (fruits, vegetables, potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat, clientid, date) VALUES ('{fruits}','{vegetables}','{potatoBags}', '{eggs}','{butter}', '{groundBeef}', '{wholeChicken}', '{veggieFrozen}', '{bread}', '{cannedVeggie}', '{cannedFruit}', '{cannedSoup}', '{cannedSeafood}', '{cannedMeat}', '{clientid}' , '{date}')".format(
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
					clientid=currentId,
					date=request.form['date']))
		else:
			error = "Too much food requested for the client's current family size"
	else:
		error = "Invalid date and time, please pick a future date and time."
	conn.commit()
	conn.close()
	return render_template('reqform.html',error=error,data=results)

@app.route('/addAppointmentData', methods=['POST'])
def addAppointmentData():
	error = None
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	volunteerExists = False
	clientExists=False
	t = (request.form['vID'])
	temp = (t,)
	for row in c.execute("SELECT * FROM Volunteer WHERE accountid=?",temp):
		volunteerExists=True
		break
	else:
		print("volunteer not found")

	t = (request.form['cID'])
	temp = (t,)
	for row in c.execute("SELECT * FROM Client WHERE accountid=?",temp):
		clientExists=True
		break
	else:
		print("client not found")
	
	t = (request.form['time'])
	print(t+" this is time from form")
	#https://stackabuse.com/converting-strings-to-datetime-in-python/
	date_time_obj = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M')
	current = datetime.datetime.now()+datetime.timedelta(days=1)

	#ensure that appointment times are at least 1 day away
	if (date_time_obj>current):
		if (volunteerExists and clientExists):
			c.execute(
				"INSERT INTO Appointment (time, clientid, volunteerid ) VALUES ('{time}', '{clientid}','{volunteerid}')".format(
					time=request.form['time'],
					clientid=request.form['cID'],
					volunteerid=request.form['vID']))
		else:
			error = "The requested Volunteer ID or Client ID does not exist."
	else:
		error = "Invalid date and time, please pick a future date and time."
	conn.commit()
	conn.close()
	return render_template('addAppointment.html',error=error)

@app.route('/addInventoryData', methods=['POST'])
def addInventoryData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	c.execute(
		"INSERT INTO Foodstore (refcode, foodname, quantity, expirydate, address) VALUES ('{refcode}','{foodname}','{quantity}', '{expirydate}', '{address}')".format(
			refcode=request.form['refcode'],
			foodname=request.form['foodname'],
			quantity=request.form['quantity'],
			expirydate=request.form['expirydate'],
			address=request.form['address']))

	conn.commit()
	conn.close()
	return redirect('/')

#client = 0, volunter = 1, admin = 2
#done
@app.route('/register', methods=['POST'])
def addClientUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	error=None
	c.execute("SELECT username FROM Account")
	results = c.fetchall()
	resultsformat = []
	for _ in results:
		resultsformat.append(_[0])
	print(resultsformat)
	print(request.form['username'] in resultsformat)
	if request.form['username'] in resultsformat:
		error="username exists please use a different username"
		return render_template('signup.html',error=error)


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

	conn.commit()
	conn.close()
	return redirect('/admin')

@app.route('/addAdmin')
def addAdmin():
	global currentUser
	if (currentUser==2):
		return render_template('addAdmin.html')
	else:
		return render_template('admin.html')

@app.route('/addAppointment')
def addAppointment():
	return render_template('addAppointment.html')

@app.route('/addDonor')
def addDonor():
	global currentUser
	if (currentUser==2):
		return render_template('addDonor.html')
	else:
		return render_template('admin.html')

#done
@app.route('/addDonorData', methods=['POST'])
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

@app.route('/addSupplierData', methods=['POST'])
def addSupplierData():

	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Supplier (name,phonenumber,email) VALUES ('{name}','{phonenumber}','{email}')".format(
			name=request.form['name'],
			phonenumber=request.form['phonenumber'],
			email=request.form['email']))
	
	conn.commit()
	conn.close()


	return redirect('/admin')

@app.route('/updateFundsData', methods=['POST'])
def updateFundsData():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	address = "251 MacEwan Student Centre 2500 University Drive NW Calgary"
	c.execute("UPDATE Foodbank SET funds = ? WHERE address = ?", (request.form['funds'],address))
	
	conn.commit()
	conn.close()
	return redirect('/admin')

@app.route('/updateFunds')
def updateFunds():


	global currentUser
	if (currentUser==2):
		return render_template('updateFunds.html')
	else:
		return render_template('admin.html')

@app.route('/addInventory')
def addInventory():

	global currentUser
	if (currentUser==2):
		return render_template('addInventory.html')
	else:
		return render_template('admin.html')

@app.route('/addSupplier')
def addSupplier():

	global currentUser
	if (currentUser==2):
		return render_template('addSupplier.html')
	else:
		return render_template('admin.html')



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

@app.route('/viewAdmin')
def viewAdmin():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Account INNER JOIN Admin ON Account.id=Admin.accountid")

	results = c.fetchall()
	print(results)

	global currentUser
	if (currentUser==2):
		return render_template('viewAdmin.html', data=results)
	else:
		return render_template('admin.html')

	
	

@app.route('/viewVolunteer')
def viewVolunteer():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Account INNER JOIN Volunteer ON Account.id=Volunteer.accountid")
	results = c.fetchall()
	print(results)

	global currentUser
	if (currentUser==2):
		return render_template('viewVolunteer.html', data=results)
	else:
		return render_template('admin.html')

#done
@app.route('/viewClient')
def viewClient():
	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM Account INNER JOIN Client ON Account.id=Client.accountid")
	results = c.fetchall()
	print(results)
	global currentUser


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

	global currentUser
	if (currentUser==2):
		return render_template('viewInventory.html',data=results)
	else:
		return render_template('admin.html')


@app.route('/viewOrder')
def viewOrder():
	#if currentUser==2 or currentUser==3:

	results = []
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT * FROM RequestForm")
	results = c.fetchall()
	print(results)
	global currentUser
	if (currentUser>0):
		return render_template('viewOrder.html', data=results)
	else:
		return redirect('/')


@app.route('/deleteAdminUser',methods=['POST'])
def deleteAdminUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Account WHERE id=?", temp)
	
	conn.commit()
	conn.close()
	return redirect('/viewAdmin')


@app.route('/deleteVolunteerUser',methods=['POST'])
def deleteVolunteerUser():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()
	t = (request.form['id'])
	temp = (t,)
	c.execute("DELETE FROM Account WHERE id=?", temp)
	
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
	return redirect('/viewAdmin')

@app.route('/deleteAdmin')
def deleteAdmin():

	global currentUser
	if (currentUser==2):
		return render_template('deleteAdmin.html')
	else:
		return render_template('admin.html')

@app.route('/deleteVolunteer')
def deleteVolunteer():

	global currentUser
	if (currentUser==2):
		return render_template('deleteVolunteer.html')
	else:
		return render_template('admin.html')

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

@app.route('/finishOrderPage')
def finishOrderPage():
	return render_template('finishOrderPage.html')



@app.route('/finishOrder', methods=['POST'])
def finishOrder():
	global currentId
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	t = (request.form['id'])
	temp = (t,)
	cursor=c.execute("SELECT clientid FROM RequestForm WHERE id=?", temp)
	clientid = cursor.fetchone()
	volunid = currentId

	print(volunid)
	print("volun id above")
	print(clientid[0])
	print("clientid above")
	c.execute("UPDATE RequestForm SET volunteerid = ? WHERE id = ?",(volunid,request.form['id']))

	t = (request.form['id'])
	temp = (t,)
	cursor = c.execute("SELECT * FROM RequestForm WHERE id=?",temp)
	requested = cursor.fetchone()
	requested = list(requested)
	requested.pop(0)
	requested = requested[:len(requested)-3]

	

	cursor = c.execute("SELECT quantity FROM Foodstore")
	currentstored = cursor.fetchall()
	currentstored = list(currentstored)
	print(currentstored)
	print("above is foodstored")
	storedformated = []
	for _ in currentstored:
		storedformated.append(_[0])


	print(requested)
	print(len(requested))
	print(storedformated)
	print(len(storedformated))

	allSmaller = True
	for _ in range(len(requested)):
		if (requested[_]>storedformated[_]):
			allSmaller = False
			break
	foodindex = 1
	if (allSmaller):
		for _ in requested:
			c.execute(
				"INSERT INTO Takes (clientid,foodbarcode,quantity) VALUES ('{clientid}','{foodbarcode}','{quantity}')".format(
					clientid=clientid[0],
					foodbarcode=foodindex,
					quantity=_))
			c.execute("UPDATE Foodstore SET quantity = quantity-? WHERE refcode = ?", (_,foodindex))
			foodindex+=1

	conn.commit()
	conn.close()
	return redirect('/viewOrder')

					
@app.route('/viewStats')
def viewStats():

	global currentUser
	if (currentUser==2):
		return render_template('viewStats.html')
	else:
		return render_template('admin.html')



@app.route('/genStatsVolunteer',methods=['POST'])
def genStatsVolunteer():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT COUNT(id) FROM Appointment WHERE ? = volunteerid", (request.form['Vid']))
	results = c.fetchall()

	return render_template('viewStatsVolunteer.html', data = results)

@app.route('/genStatsClient',methods=['POST'])
def genStatsClient():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT COUNT(id) FROM Appointment WHERE ? IN (SELECT accountid FROM Client)", (request.form['Cid']))
	results = c.fetchall()

	return render_template('viewStatsClient.html', data = results)

@app.route('/genStatsAllClient',methods=['POST'])
def genStatsAllClient():
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute("SELECT COUNT(id) FROM Appointment WHERE clientid IN (SELECT accountid FROM Client WHERE income <= 10000)")
	results = c.fetchall()

	return render_template('viewStatsAllClient.html', data = results)

