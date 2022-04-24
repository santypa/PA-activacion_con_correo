from re import U
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import usuariosmodels
from models import archivo
from controller import ingreso
from controller import guardarimagenes
from controller import registrarusuario
from controller import correo
from controller import cambiapas
from controller import sesion



app = Flask(__name__) 
app.secret_key = "sdasdasdasd"

@app.get("/")  
def login():
    if 'usuario_id' in session:
        archivos = archivo.obtenerarchivo()
        return render_template("archivos.html", archivos=archivos)
   
    return render_template("login.html")
    
@app.post("/") 
def ingresar():
    if 'usuario_id' in session:
        archivos = archivo.obtenerarchivo()
        return render_template("archivos.html", archivos=archivos)
    
    if ingreso.validaringreso(email=request.form.get('email'),password = request.form.get('password')):
        return render_template("login.html",email=request.form.get('email'),password = request.form.get('password')) 
    
    return render_template("login.html",email=request.form.get('email')) 
    
@app.get("/muestra")
def mostrar():
   return render_template("inicio.html") 
 
@app.get("/crear")
def crearUsuario():
    return render_template("crear.html")

@app.post("/crear")
def crearUsuarioPost():
    if registrarusuario.registrar(nombre = request.form.get('nombre'),email = request.form.get('email'),password = request.form.get('password')):
        return render_template("crear.html",nombre = request.form.get('nombre'),email = request.form.get('email'),password = request.form.get('password'))
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
def recuperarcontrapost():
    if correo.sicorreo(direccion = request.form.get('email')):
        return render_template("recuperar.html",direccion = request.form.get('email'))
    return render_template("login.html")
    
@app.route("/restablecer/<toke>")
def contrapost(toke):
    if toke != None:
        return render_template("restablecer.html",toke=toke)
    return render_template("recuperarcontra")
    
@app.get("/contraupdates")
def contraup():  
    return render_template("establecer.html")
    
@app.post("/contraupdates")
def contraupdate():
    if cambiapas.cambiarpass(password1 = request.form.get('password1'),password = request.form.get('password'),toke = request.form.get('toke')):
        return render_template("login.html")
    return render_template("restablecer.html",password = request.form.get('password'),toke = request.form.get('toke'))
    
app.run(debug=True)
