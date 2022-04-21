
from flask import Flask, render_template, request, redirect, url_for, flash, session
from controller import validarcorreo
from models import usuariosmodels
from controller import send_main

def registrar(nombre,email,password):
    
    valido1 = validarcorreo.validarlog(nombre=nombre,email=email,password=password)
    valido = validarcorreo.correovalido(email=email)
    usuario = usuariosmodels.verificarusuario(email=email)
    valor=validarcorreo.redir(usuario=usuario,valido1=valido1,valido=valido,nombre=nombre,email=email,password=password)
    
    if valor == True:
        return render_template("crear.html", nombre=nombre, email=email, password=password)
    
    usuariosmodels.crearusuario(nombre=nombre, email=email, password=password)
    
    direccion = email
    send_main.correo(direccion=direccion) 
    return