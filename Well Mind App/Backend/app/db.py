import sqlite3

def create_db():
    conn = sqlite3.connect('wellmind.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT, emotion TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS biometrics
                      (user_id INTEGER, heart_rate INTEGER, sleep_hours REAL)''')
    conn.commit()
    conn.close()

def add_user_checkin(user_id, emotion):
    conn = sqlite3.connect('wellmind.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, username, emotion) VALUES (?, ?, ?)", 
                   (user_id, "user_name", emotion))
    conn.commit()
    conn.close()

def add_biometric_data(user_id, heart_rate, sleep_hours):
    conn = sqlite3.connect('wellmind.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO biometrics (user_id, heart_rate, sleep_hours) VALUES (?, ?, ?)", 
                   (user_id, heart_rate, sleep_hours))
    conn.commit()
    conn.close()
