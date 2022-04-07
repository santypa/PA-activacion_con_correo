from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash

def obtenerUsuario():

    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from usuarios")
    usuario = cursor.fetchall()
    cursor.close()

    return usuario


def ingresoUsuario(nombre, password):

    print(password+nombre)
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * from usuarios where nombre = %s and password = %s", (
        nombre,
        password
    ))
    usuario = cursor.fetchone()
    cursor.close()

    return usuario


def crearusuario(nombre, email, password):


    password=generate_password_hash(password)
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios(nombre,email,password) VALUES (%s,%s,%s)", (
        nombre,
        email,
        password
    ))
    cursor.close()
 
