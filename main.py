from flask import Flask, render_template, request, redirect, url_for, flash
from models import usuariosmodels

app = Flask(__name__) #instancia python.
app.secret_key = "sdasdasdasd"



@app.get("/")  #funcion decoradora crea una ruta.
def login():    
    return render_template("login.html")

@app.post("/")  #funcion decoradora crea una ruta.
def ingresar():  
    
    
    nombre = request.form.get('nombre')
    password = request.form.get('password')
    
    if nombre == "":
        flash("este campo es obligatorio")
        
    if password == "":
        flash("este campo es obligatorio")
    
    
    ''' usuariosmodels.ingresoUsuario(nombre=nombre,password=password) '''
    
    usuario = usuariosmodels.ingresoUsuario(nombre=nombre,password=password)
    ''' print(usuario) '''
    
    if usuario == []:
        return render_template("login.html")

    return render_template("inicio.html",usuario=usuario)

@app.get("/crear")
def crearUsuario():
    return render_template("crear.html")


@app.post("/crear")
def crearUsuarioPost():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    
    isValid = True
    
    if nombre == "":
        isValid = False
        flash("este campo es obligatorio")
        
    if email == "":
        isValid = False
        flash("este campo es obligatorio")
       
    if password == "":
        isValid = False
        flash("este campo es obligatorio")
        
    
    if isValid == False:
        return render_template("crear.html",nombre=nombre,email=email,password=password)
    
    usuariosmodels.crearusuario(nombre=nombre,email=email,password=password)
    return render_template("login.html")

    #return redirect(url_for("/"))

app.run(debug=True)

