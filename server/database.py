import sqlite3

def create_connection():
    return sqlite3.connect('users.db')

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL, 
            password TEXT NOT NULL,
            status TEXT DEFAULT 'offline'
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    returnMessage = ""
    
    try:
        c.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        conn.commit()
        returnMessage = "User registered successfully"
    except sqlite3.IntegrityError:
        returnMessage = "Error: Username already exists"
        
    conn.close()
    return returnMessage

def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    returnMessage = ""
    
    c.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = c.fetchone()
    if user:
        c.execute('''
            UPDATE users SET status = 'online' WHERE username = ?
        ''', (username,))
        conn.commit()
        returnMessage = "Login successful"
    else:
        returnMessage = "Error: Invalid credentials"
        
    conn.close()
    return returnMessage

def get_online_users():
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('''
        SELECT username FROM users WHERE status = 'online'
    ''')
    users = c.fetchall()
    
    conn.close()
    return users

def logout_user(username):
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('''
        UPDATE users SET status = 'offline' WHERE username = ?
    ''', (username,))
    conn.commit()
    
    conn.close()
    return "Logout successful"