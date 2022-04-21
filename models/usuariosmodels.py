from asyncio.windows_events import NULL
from sqlalchemy import false
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash,session

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
    cursor.close()
    
    if user != None:
       valor = False
       flash("El correo ya tiene un usuario registrado")
       
    return valor

def ingresoUsuario(email, password):

    pas=False
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT  id,nombre,PASSWORD,activo  from usuarios WHERE email = %s",(email,))
    usuario = cursor.fetchall()
    cursor.close()
    

    for passw in usuario:
        
        pas=check_password_hash(passw["PASSWORD"],password)
        
        if pas == True:
            if passw["activo"] != None:
                session['usuario_id'] = passw["id"]
                return render_template("inicio.html",usuarios=passw)
                
            else:
                flash("Falta activacion")
        else:
            flash("Usuario o Paswword incorrectos")
            return render_template("login.html")
        
    return passw

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

def activar(url,toke):
    
    cursor = db.cursor(dictionary=True)
    if url != None:
        print()
        cursor = db.cursor(dictionary=True)
        cursor.execute("UPDATE usuarios SET activo = 'activo' WHERE email = (%s)",(
          toke,  
        ))
        cursor.close()
        
    return
#comparar la encriptacion con la original
    #print(check_password_hash(password,password))