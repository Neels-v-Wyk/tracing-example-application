import psycopg2
import random, time

from ddtrace import tracer
from flask import Flask, request
from passlib.hash import pbkdf2_sha256

# Initialize dummy data in the DB

pg_conn = psycopg2.connect(
    host='postgres',
    database='postgres',
    user='postgres',
    password='pgpass'
)
pg_conn.autocommit = True
pg_cur = pg_conn.cursor()

pg_cur.execute("create table if not exists logins (username TEXT, password TEXT)")
pg_cur.execute("TRUNCATE TABLE logins")

# Generated with faker, but pasted in so we can have some overlap with the client
logins = [
    ('lalexander', 'x5Q0a@k)+)'),
    ('deanstephanie', '_8H5WdQqym'),
    ('julia66', 'THQXpuO&%6'),
    ('ruizpatrick', '#+9#UN#uHM'),
    ('david87', 'u%3dM4UfI0'),
    ('padillatyler', 'Vp_6KFQuH+'),
    ('wellsjoseph', '3B3G)NpP^Y'),
    ('lindaherrera', 'D6E7csFM#1'),
    ('michael54', 'U5sL&2Jn^X'),
    ('aking', 'k)X3KjbV_8'),
    ('jeffreyfaulkner', 'w4D(ogjj$e'),
    ('debraaustin', 'ZD+wV9Mr2s'),
    ('jacksonedward', '&965zS4a80'),
    ('cruzmichelle', '!0ktPm&eJc'),
    ('galvanjohn', '3nYS(ola(8'),
]
logins = [(x[0], pbkdf2_sha256.hash(x[1])) for x in logins] # Hash the logins

pg_cur.executemany("INSERT INTO logins(username, password) VALUES(%s, %s)", logins)


# Run app server
app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    # Simulate up to 50 ms delay
    time.sleep(random.random() / 20)

    data = request.json
    pg_cur.execute("select username, password from logins where username = %s", (data['username'],))
    res = pg_cur.fetchall()
    if len(res) != 1: # Invalid pass
        return "Invalid username", 401
    
    if pbkdf2_sha256.verify(data['password'], res[0][1]):
        return "Valid login", 200
    else:
        return "Invalid password", 401


app.run(host='0.0.0.0', port=5000)
