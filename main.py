from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import usuariosmodels
from models import validarcorreo
from models import validarlogin
from models import send_main


app = Flask(__name__)  # instancia python.
app.secret_key = "sdasdasdasd"


@app.get("/")  # funcion decoradora crea una ruta.
def login():
    
    if 'usuario_id' in session:
        return render_template("inicio.html")
    
    return render_template("login.html")

@app.post("/")  # funcion decoradora crea una ruta.
def ingresar():

    email = request.form.get('email')
    password = request.form.get('password')

    if email == "":
        flash("este campo es obligatorio")

    if password == "":
        flash("este campo es obligatorio")


    usuario = usuariosmodels.ingresoUsuario(email=email, password=password)
    
    if usuario == None:
        flash("Usuario o Paswword incorrectos")
        return render_template("login.html")
    
    if usuario != None:
        if usuario['activo'] == None:
            flash("El usuario no esta activo")
            return render_template("login.html")
        
    session['usuario_id']= usuario['id']
   
    
        
    if 'usuario_id' in session:
        return render_template("inicio.html",usuario=usuario)
    
    return render_template("login.html",usuario=usuario) 
    #return render_template("inicio.html", usuario=usuario)

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
    
    return render_template("inicio.html")

''' @app.post("/añadir")
def guardarimagen():
    
    imagen = request.files['imagen']
    imagen.save('./static/image/'+imagen.filename)
    #imagen.save(imagen.filename)
    usuariosmodels.crearimagen(imagen=imagen)
    
    return render_template("inicio.html") '''


@app.get("/limpiar")
def cerrarsesion():
    session.clear()
    return redirect(url_for('login'))
    
    
app.run(debug=True)
