from trace import Trace
from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash
from re import T
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash


def correovalido(email):
    signos = ['.', '_', '-']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    dominios = ['gmail', 'hotmail', 'msn', 'yahoo', 'outlook', 'live']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mayusculas = []
    extensiones = ['com', 'net', 'com.ex', 'ea', 'es', 'mx', 'org', 'job']

    for x in minusculas:
        mayusculas.append(x.upper())

    problema = ""

    if email.find('@') !=-1:
        nuevo_email = email.split('@')
        usuario = nuevo_email[0]
        resto = nuevo_email[1]
        continuacion = resto.split('.')
        dominio = continuacion[0]
        terminacion = continuacion[1]

        for x in usuario:
            if x in signos or x in numeros or x in minusculas or x in mayusculas:
                if dominio in dominios:
                    if terminacion in extensiones:
                        valido = True
                    else:
                        valido = False
                else:
                    valido = False
            else:
                valido = False

    else:
        valido = False
    
    if valido == False:
        flash("El correo no es Valido ... Verifique el correo... ") 

    return valido

def validarlog(nombre,email,password):
    
    
    minusculas = False
    mayusculas = False
    numeros = False
    especial = False
    

    if nombre == "":
        valor = False
        flash("este campo es obligatorio")

    if email == "":
        valor = False
        flash( "este campo es obligatorio")

    if password == "":
        valor = False
        flash("este campo es obligatorio")

    for d in password:
        if d.islower() == True:
            minusculas = True
            valor = True  
        if d.isupper() == True:
            mayusculas = True
            valor = True                
        if d.isdigit() == True:
            numeros = True
            valor = True

    if re.search('[@_|!#$%&/()=><:¡?°¿*]',password):
        especial = True
    
    if especial == False:
        flash("faltan caracteres especiales")
        valor = False
        
    if minusculas == False:
        flash("faltan minusculas")
        valor = False
    if mayusculas == False:
        flash("faltan mayusculas")
        valor = False
    if numeros == False:
        flash("faltan numeros")
        valor = False 
        
    if len(password) < 8:
        flash("contraseña muy corta")
        valor = False
        
    return valor

def redir(usuario,valido1,valido,nombre,email,password):
    
    isValid1=valido1
    isValid=valido
    
    
    valor = False
    if isValid == False or isValid1 == False or usuario == False :
        valor = True
        
    return valor


#comparar la encriptacion con la original
#print(check_password_hash(password,password))