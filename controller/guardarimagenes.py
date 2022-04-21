from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import archivo

def guardar(nombre,imagen):
    
    isValid = True
    nombre = request.form.get('nombre')
    imagen = request.files['imagen']
    if nombre == "":
        isValid = False
        flash("el nomre es obligatorio")  
        
    if isValid == False:
        return render_template("inicio.html", nombre=nombre)
    
    idpersona = session["usuario_id"]
    
    imagen.save('./static/image/'+ imagen.filename)
    
    archivo.guardararchivo(idpersona=idpersona, nombre=nombre, imagen='/static/image/'+ imagen.filename)
    
    
    return 