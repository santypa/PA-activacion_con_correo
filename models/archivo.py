from email.mime import image
from requests import session
from config.database import db
from flask import Flask, render_template, request, redirect, url_for, flash, session

def obtenerarchivo():

    persona= session["usuario_id"]
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id_imagen = %s ",(
        persona,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
    
    return archivos


def guardararchivo(idpersona,nombre, imagen):
    
    cursor = db.cursor() 
    cursor.execute("INSERT into imagenes(nombre,img,id_imagen) values (%s,%s,%s)", (
        nombre,
        imagen,
        idpersona
    ))
    cursor.close()    
    