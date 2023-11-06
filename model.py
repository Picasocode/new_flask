import sqlite3 as sql

def insertUser(username,password,email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,username,password) VALUES (?,?,?)", (email,username,password))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users
def create_database():
    con = sql.connect('food.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY,
            restaurant_name TEXT,
            food_name TEXT,
            quantity INTEGER,
            email TEXT,
            phone TEXT
        )
    ''')
    con.commit()
    con.close()

def create_ngo_database():
    con = sql.connect('ngo.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ngo (
            id INTEGER PRIMARY KEY,
            ngo_name TEXT,
            contact_person TEXT,
            email TEXT,
            phone TEXT,
            food_items_needed TEXT
        )
    ''')
    con.commit()
    con.close()

