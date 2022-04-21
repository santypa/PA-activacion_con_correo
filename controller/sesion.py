from flask import Flask, render_template, request, redirect, url_for, flash, session

def sesion(direccion):
    
    print(session["usuario_id"])
    if  session["usuario_id"] != None:
        return url_for(direccion)
        #return render_template("inicio.html")
        
    return