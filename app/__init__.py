"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaam2e7avj5o497811g-a.oregon-postgres.render.com",
        database="todo_gxj9",
        user="todo_gxj9_user",
        password="8yQ0Exc7LcXS25BeiLqiFvAGZtzJCsrp")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
