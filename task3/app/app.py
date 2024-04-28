import requests
from flask import Flask
from datetime import datetime
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stats
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT UNIQUE,
                 seq INTEGER DEFAULT 0)''')
    c.execute("INSERT INTO stats (name) VALUES ('time_access_count')")
    conn.commit()
    conn.close()


@app.route('/time')
def get_time():
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    current_time = response.json()['datetime']

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("UPDATE stats SET seq = seq + 1 WHERE name = 'time_access_count'")
    conn.commit()
    conn.close()

    return current_time


@app.route('/statistics')
def get_statistics():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT seq FROM stats WHERE name = 'time_access_count'")
    result = c.fetchone()
    count = result[0] if result else 0
    conn.close()

    return str(count)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
