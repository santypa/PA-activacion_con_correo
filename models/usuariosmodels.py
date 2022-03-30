from config.database import db

def obtenerUsuario():   
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from usuarios")
    usuario = cursor.fetchall()
    cursor.close()
    
    return usuario

def crearusuario(nombre,email,password):
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios(nombre,email,password) VALUES (%s,%s,%s)",(
        nombre,
        email,
        password
    ))
    
    cursor.close()
    