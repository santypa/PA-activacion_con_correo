from sqlalchemy import false
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash

def obtenerUsuario():

    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from usuarios")
    usuario = cursor.fetchall()
    cursor.close()

    return usuario


def verificarusuario(email):
    valor = True
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * from usuarios where email = %s", (
        email,
    ))
    
    user = cursor.fetchone()
    print(user)
    cursor.close()
    
    if user != None:
       valor = False
       flash("El correo ya tiene un usuario registrado")
       
    return valor

def ingresoUsuario(email, password):

   
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * from usuarios where email = %s and password = %s", (
        email,
        password
    ))
    usuario = cursor.fetchone()
    cursor.close()

    return usuario


def crearusuario(nombre, email, password):

    password=generate_password_hash(password)
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios(nombre,email,password) VALUES (%s,%s,%s)", (
        nombre,
        email,
        password
    ))
    cursor.close()
 
def crearimagen(imagen):
    cursor = db.cursor(dictionary=True)
    cursor.execute("insert INTO usuarios(imagen) values (%s)", (
        imagen
    ))
    cursor.close()

    return 
