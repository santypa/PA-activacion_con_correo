from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash
from models import usuariosmodels
from models import validarcorreo
from models import validarlogin


app = Flask(__name__)  # instancia python.
app.secret_key = "sdasdasdasd"


@app.get("/")  # funcion decoradora crea una ruta.
def login():
    return render_template("login.html")


@app.post("/")  # funcion decoradora crea una ruta.
def ingresar():

    email = request.form.get('email')
    password = request.form.get('password')

    if email == "":
        flash("este campo es obligatorio")

    if password == "":
        flash("este campo es obligatorio")

    usuario= usuariosmodels.ingresoUsuario(email=email, password=password)
    
    if usuario == None:
        flash("Usuario o Paswword incorrectos")
        return render_template("login.html")
    
    print(usuario['activo'])
    
    if usuario != None:
        if usuario['activo'] == None:
            flash("El usuario no esta activo")
            return render_template("login.html")

    return render_template("inicio.html", usuario=usuario)


@app.get("/crear")
def crearUsuario():
    return render_template("crear.html")


@app.post("/crear")
def crearUsuarioPost():
    
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    direccion = request.form.get('email')
    
    valido1 = validarcorreo.validarlog(nombre=nombre,email=email,password=password)
    valido = validarcorreo.correovalido(email=email)

    valor=validarcorreo.redir(valido1=valido1,valido=valido,nombre=nombre,email=email,password=password)
    if valor == True:
        return render_template("crear.html", nombre=nombre, email=email, password=password)
    
    
    usuariosmodels.crearusuario(nombre=nombre, email=email, password=password)

    ''' asunto = "ESTE es el asunto"
    usuariosmodels.enviarcorreo(direccion=direccion, asunto=asunto)
     '''
    return render_template("login.html")

app.run(debug=True)
