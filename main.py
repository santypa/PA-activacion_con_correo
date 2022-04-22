from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import usuariosmodels
from models import archivo
from controller import ingreso
from controller import guardarimagenes
from controller import registrarusuario
from controller import sesion

app = Flask(__name__) 
app.secret_key = "sdasdasdasd"

@app.get("/")  
def login():
    #sesion.sesion(direccion='login')
    if 'usuario_id' in session:
        return render_template("inicio.html")
    return  render_template("login.html")

@app.post("/") 
def ingresar():
    
    if 'usuario_id' in session:
       return render_template("inicio.html")

    if ingreso.validaringreso(email=request.form.get('email'),password = request.form.get('password')):
        return render_template("inicio.html")
    
    return render_template("login.html") 
    
@app.get("/crear")
def crearUsuario():
    return render_template("crear.html")

@app.post("/crear")
def crearUsuarioPost():
    registrarusuario.registrar(nombre = request.form.get('nombre'),email = request.form.get('email'),password = request.form.get('password'))
    return render_template("login.html")

@app.get("/añadir")
def guardarimagen():
    archivos = archivo.obtenerarchivo()
    return render_template("archivos.html", archivos=archivos)

@app.post("/añadir")
def guardarimagenpost():
    guardarimagenes.guardar(nombre = request.form.get('nombre'),imagen = request.files['imagen'])
    return redirect(url_for('guardarimagen'))
    
@app.get("/limpiar")
def cerrarsesion():
    session.clear()
    return render_template("login.html")
     
@app.route("/activar/<url>/<toke>")
def activar(url,toke):
    usuariosmodels.activar(url=url,toke=toke)
    return redirect(url_for("ingresar"))     

@app.get("/recuperar")
def recuperarcontra():
     return render_template("recuperar.html")
 
@app.post("/recuperar")
def recuperarcontrapost(email):
     return render_template("recuperar.html")
    

app.run(debug=True)
