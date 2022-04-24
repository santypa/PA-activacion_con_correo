
from flask import Flask, render_template, request, redirect, url_for, flash, session
from controller import validarcorreo
from models import usuariosmodels
from controller import send_main
from controller import token
from models import cargarpas

def registrar(nombre,email,password):
    
    valido1 = validarcorreo.validarlog(nombre=nombre,email=email)
    correo = validarcorreo.validarpas(password=password)
    valido = validarcorreo.correovalido(email=email)
    usuario = usuariosmodels.verificarusuario(email=email)
    valor=validarcorreo.redir(usuario=usuario,valido1=valido1,valido=valido,correo=correo)
    
    if valor == True:
        return render_template("crear.html", nombre=nombre, email=email, password=password)
    else:
        usuariosmodels.crearusuario(nombre=nombre, email=email, password=password)
        direccion = email
        valor = 1
        toke = token.acortarPost()
        cargarpas.cargartokenpassword(direccion=email,toke=toke)
        send_main.correo(direccion=direccion,valor=valor,toke=toke) 
    
    return