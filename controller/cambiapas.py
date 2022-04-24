from flask import Flask, render_template, request, redirect, url_for, flash, session
from controller import validarcorreo
from werkzeug.security import generate_password_hash, check_password_hash
from models import cargarpas

def cambiarpass(password1,password,toke):
    if password == password1:
          pas = validarcorreo.validarpas(password=password)
          if pas == True:
            password = generate_password_hash(password)
            cargarpas.cargarpassword(password=password,toke=toke)            
            return url_for("login")
    else: 
          flash("La contraseña no es la misma")  
    return