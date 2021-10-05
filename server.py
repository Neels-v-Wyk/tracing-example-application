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
