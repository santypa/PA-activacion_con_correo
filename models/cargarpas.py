
from config.database import db

def cargarpassword(password,toke):
   
    cursor = db.cursor() 
    cursor.execute("UPDATE usuarios SET PASSWORD = %s WHERE toke = %s ", (
      password,
      toke  
    ))
    usuario = cursor.fetchall()
    cursor.close() 
    print(usuario)
    return

def validausuario(direccion):
      
  cursor = db.cursor(dictionary=True)
  cursor.execute("SELECT  * from usuarios WHERE email = %s",(
        direccion,
  ))
  usuario = cursor.fetchall()
  cursor.close()
    
  return usuario

def cargartokenpassword(direccion,toke):
  print(direccion,toke)
  cursor = db.cursor(dictionary=True)
  cursor.execute("UPDATE usuarios SET `toke`= %s where email = %s",(
        toke,
        direccion
  ))
  cursor.close()
      
  return

