from cgi import print_arguments
from email.mime import image
from requests import delete, session
from config.database import db
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

def obtenerarchivo(id):
  
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id_imagen = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
    
    return archivos

def guardararchivos(idpersona,nombre, imagen):
    
    
    cursor = db.cursor() 
    cursor.execute("INSERT into imagenes(nombre,img,id_imagen) values (%s,%s,%s)", (
        nombre,
        imagen,
        idpersona
    ))
    cursor.close()    
    
def eliminararchivo(id):
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imagenes WHERE id = %s ",(
        id,
    )) 
    archivo = cursor.fetchall() 
    cursor.close()
    
    #os.remove(archivo[0]['img'])
    
    print("eliminar")
    print(archivo[0]["img"])
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("DELETE FROM imagenes WHERE id = %s ",(
        id,
    )) 
    cursor.close()
    
    return
    
def editararchivo(id):
    
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
 
    return archivos

def guardararchivo(nombre, imagen,id):
    
    cursor = db.cursor() 
    cursor.execute("UPDATE imagenes SET nombre= %s , img= %s WHERE  id = (%s)", (
        nombre,
        imagen,
        id
    ))
    cursor.close()  

def misarchvios(id):
    cursor= db.cursor(dictionary=True)
    cursor.execute("SELECT * from imagenes where id = %s ",(
        id,
    ))
    archivos = cursor.fetchall()   
    cursor.close()
    
    return archivos