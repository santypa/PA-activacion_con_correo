from xml.dom.minidom import Identified
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import usuariosmodels
from controller import validarcorreo
from controller import send_main
from models import archivo
from controller import token
from controller import ingreso
from controller import sesion
import string
import random
from config.database import db

app = Flask(__name__) 
app.secret_key = "sdasdasdasd"

@app.get("/")  
def login():
    
    if 'usuario_id' in session:
       return render_template("inicio.html")
    #sesion.sesion(direccion='login')
    return  render_template("login.html")

@app.post("/") 
def ingresar():
    
    if 'usuario_id' in session:
       return render_template("inicio.html")
    
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "":
        flash("este campo es obligatorio")

    if password == "":
        flash("este campo es obligatorio")

    
    usuario = usuariosmodels.ingresoUsuario(email=email, password=password)
    
    return render_template("login.html",usuario=usuario) 
    

@app.get("/crear")
def crearUsuario():
    return render_template("crear.html")


@app.post("/crear")
def crearUsuarioPost():
    
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    valido1 = validarcorreo.validarlog(nombre=nombre,email=email,password=password)
    valido = validarcorreo.correovalido(email=email)
    usuario = usuariosmodels.verificarusuario(email=email)
    valor=validarcorreo.redir(usuario=usuario,valido1=valido1,valido=valido,nombre=nombre,email=email,password=password)
    
    if valor == True:
        return render_template("crear.html", nombre=nombre, email=email, password=password)
    
    
    usuariosmodels.crearusuario(nombre=nombre, email=email, password=password)
    
    
    direccion = email
    send_main.correo(direccion=direccion) 
    
    return render_template("login.html")


@app.get("/añadir")
def guardarimagen():
    
    archivos = archivo.obtenerarchivo()

    return render_template("archivos.html", archivos=archivos)


@app.post("/añadir")
def guardarimagenpost():
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
    
    return redirect(url_for('guardarimagen'))
    

@app.get("/limpiar")
def cerrarsesion():
    session.clear()
    return render_template("login.html")
     

@app.route("/activar/<url>/<toke>")
def activar(url,toke):
    usuariosmodels.activar(url=url,toke=toke)
    return redirect(url_for("ingresar"))     


app.run(debug=True)
