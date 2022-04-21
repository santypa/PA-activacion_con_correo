from flask import Flask, render_template, request, redirect, url_for, flash, session
from email.mime import image
from requests import session
from config.database import db


def sesion(direccion):
    
    print(session["usuario_id"])
    if  session["usuario_id"] != None:
        return url_for(direccion)
        #return render_template("inicio.html")
        
    return