from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import archivo
import os

def guardar(nombre,imagen):
    
    if nombre == "":
        flash("el nomre es obligatorio")  
        return render_template("inicio.html", nombre=nombre)
        
    idpersona = session["usuario_id"]
    imagen.save('./static/image/'+ imagen.filename)
    filename = ('./static/image/'+ imagen.filename)
    print("este es el preso del archivo")
    peso=os.path.getsize(filename)
    print(peso%1024)
    archivo.guardararchivos(idpersona=idpersona, nombre=nombre, imagen='/static/image/'+ imagen.filename)
    return 

def updateimagen(nombre,imagen,id):
    imagen.save('./static/image/'+ imagen.filename)
    archivo.guardararchivo(nombre=nombre, imagen='/static/image/'+imagen.filename,id=id)
    
    return