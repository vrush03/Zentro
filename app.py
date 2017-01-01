from flask import Flask, render_template, json, request, redirect, session
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tekken5'
app.config['MYSQL_DATABASE_DB'] = 'zentro'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def main():
	print "hello"
	if request.method == 'POST':    
		firstname = str(request.form['fname'])
		lastname = str(request.form['lname'])
		email = str(request.form['email'])
		flag = str(request.form['delivery'])
		flat = str(request.form['flat'])
		society = str(request.form['society'])
		landmark = str(request.form['landmark'])
		pincode = int(request.form['pincode'])
		mobNo = str(request.form['mobileNo'])
		detail = str(request.form['message'])
		conn = mysql.connect()
		curr = conn.cursor()
		#curr.execute("Insert into Order (Detail, MobileNo, PINCODE, Landmark, Society, Flat, Place, FirstName, LastName, Useremail) values(%s,%d,%d,%s,%s,%s,%s,%s,%s,%s)",detail,mobNo,pincode,landmark,society,flat,flag,firstname,lastname,email)
		curr.callproc('sp_addStat',(detail,mobNo,pincode,landmark,society,flat,flag,firstname,lastname,email))
		conn.commit()
		curr.close()
		conn.close()
		#lastname  = str(request.form['lname'])
	#print firstname
	return render_template('index.html')

@app.route("/database", methods=['GET', 'POST'])
def getData():
	conn = mysql.connect()
	curr = conn.cursor()
	curr.execute("Select * from Order1")
	data = curr.fetchall()
	#print data[0],data[1]
	data_dict = []
	for i in data:
			#print i
			data_dic = {
			'Detail': i[0],
			'MobileNo': i[1],
			'PINCODE': i[2],
			'Landmark': i[3],
			'Society': i[4],
			'Flat': i[5],
			'Place' : i[6],
			'FirstName' : i[7],
			'LastName' : i[8],
			'Useremail' : i[9],
			}
			data_dict.append(data_dic)
			#print i
			#print data_dic
	
	#print data_dict
	finData = data_dict
	conn.commit()
	curr.close()
	conn.close()
	return render_template('admin.html',loopdata = finData)


if __name__ == "__main__":
    app.debug = True
    #print "Hello"
    app.run()
