from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import model as dbHandler
import sqlite3

app = Flask(__name__)
@app.route('/home')
def home():
       return render_template("ngo_requests.html")
@app.route('/signup_api', methods=['POST', 'GET'])
def signup_api():
    if request.method=='POST':
           username = request.form['username']
           password = request.form['password']
           email=request.form['email']
           dbHandler.insertUser(username, password,email)
           return redirect("/")
    else:
           return render_template('error.html')

@app.route('/login_api', methods=['POST', 'GET'])
def login_api():
    if request.method=='POST':
           username = request.form['username']
           password = request.form['password']
           users=dbHandler.retrieveUsers()
           if (username,password) in users:
            return redirect('/home')
           else:
            return render_template('error.html')

@app.route('/')
def login():
       return render_template("login.html")

@app.route('/signup')
def signup():
       return render_template("signup.html")

@app.route('/logout')
def logout():
       return redirect('/')



@app.route('/ngo_requests', methods=['GET', 'POST'])
def ngo_request():
    dbHandler.create_ngo_database()
    if request.method == 'POST':
        ngo_name = request.form['ngo_name']
        contact_person = request.form['contact_person']
        email = request.form['email']
        phone = request.form['phone']
        food_items_needed = request.form['food_items']

        conn = sqlite3.connect('ngo.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ngo (ngo_name, contact_person, email, phone, food_items_needed) VALUES (?, ?, ?, ?, ?)',
                       (ngo_name, contact_person, email, phone, food_items_needed))
        conn.commit()
        conn.close()

        return redirect(url_for('list_ngo_requests'))

    return render_template('ngo_requests.html')

# Route to display NGO requests
@app.route('/ngo_list')
def list_ngo_requests():
    conn = sqlite3.connect('ngo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ngo')
    ngo_data = cursor.fetchall()
    conn.close()

    return render_template('ngo_list.html', ngo_data=ngo_data)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port="4000")