import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database="login",
    port="3306"
)

db.autocommit = True
