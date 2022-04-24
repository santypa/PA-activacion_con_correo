from controller import token
from config.database import db
from controller import send_main
from models import cargarpas
from flask import Flask, render_template, request, redirect, url_for, flash, session

def sicorreo(direccion):
    usuario = cargarpas.validausuario(direccion=direccion)
    if usuario == []:
        flash("el nomre del correo no existe")
        return render_template("recuperar.html",direccion = direccion)
    
    toke = token.acortarPost()
    cargarpas.cargartokenpassword(direccion=direccion,toke=toke)
    send_main.correo(direccion = direccion,valor=2,toke=toke)
    
    return 
        
    