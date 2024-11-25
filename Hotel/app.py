from flask import Flask,render_template,redirect,request,url_for
# from flask_mysqldb import MySQL
import mysql.connector

app=Flask(__name__,template_folder='templates', static_folder='static',static_url_path="/" )
app.secret_key='swetha project'

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="Hotel_Room_Management1",
    user="root",
    password="1234"
)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/room')
def room():
    # print(mysql.connection)
    cur = connection.cursor()
    cur.execute("SELECT * FROM RoomDetails")
    empinfo = cur.fetchall()
    cur.close()
    return render_template('RoomManagement.htm',Rooms=empinfo)

@app.route('/search',methods= ['POST', 'GET'])
def search():
    search_results = []
    search_term=''
    if request.method == "POST":
        search_term=request.form['roomNo']
        cur = connection.cursor()
        query="SELECT * FROM RoomDetails WHERE roomNo like %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results=cur.fetchmany(size=1)
        cur.close()
        return render_template('RoomManagement.htm',Rooms=search_results)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        iddata= request.form['roomNo']
        name = request.form['name']
        email = request.form['email']
        dept = request.form['phone']
        cur = connection.cursor()
        cur.execute("INSERT INTO RoomDetails (roomNo,name,email,phone) VALUES (%s,%s,%s,%s)", (iddata,name,email,dept,))
        connection.commit()
        return redirect(url_for('room'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cur = connection.cursor()
    cur.execute("DELETE FROM RoomDetails WHERE roomNo=%s", (id_data,))
    connection.commit()
    return redirect(url_for('room'))

@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        print("Entered")
        id_data = request.form['roomNo']
        name = request.form['name']
        email = request.form['email']
        dept = request.form['phone']

        cur = connection.cursor()
        print("Cursor created")
        cur.execute("UPDATE RoomDetails SET name=%s,email=%s,phone=%s WHERE roomNo=%s", (name,email,dept,id_data))
        connection.commit()
        return redirect(url_for('room'))


if __name__=="__main__":
    app.run(debug=True)