
def correo(direccion,valor,toke):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from msilib.schema import MIME
    from flask import request
    from config import settings
    from email import message
    from http import server
    from cgitb import html
    from smtplib import SMTP
    from email.message import EmailMessage
    from typing_extensions import Required

    message = EmailMessage()
    message = MIMEMultipart("alternative")
    
    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD
    
    message['Subject'] = "CODIGO DE ACTIVACION"
    message['From'] = username
    message['To'] = direccion


    if valor == 1:
        
        html = f"""
<HTML>
    <HEAD>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
        <title>ACTIVAR</title>
    </HEAD>
    <BODY style=" background-color: powderblue; align-self: baseline; text-align: center;">
        <div class="text-center">
        <div class="card border-primary mb-3 ">
            <div class="card-header ">
                <h1 class="text-center " style="font-family: 'Times New Roman', Times, serif;background-color: DodgerBlue;">ACTIVAR SESION</h1>
                 </div>
            <div class="card-body">
                <figcaption class="blockquote-footer">
                    <h5 class="card-title">Hola -- Bienvenido : <br><cite title="Source Title"> {direccion} </cite><br> </h5>
                </figcaption>
                <p class="card-text" style="border: 1px solid rgb(91, 174, 185);">
                    para poder realizar la activacion  <br>
                    de inicio de sesion por favor presione el <br>
                    siguiente boton... </p>
                <div class="text-center">
                    <a style="outline: none;text-decoration: none;display: inline-block;width: 19.5%;margin-right: 0.625%;text-align: center;line-height: 3;color: black;background:silver;" class="button btn-primary" href='http://127.0.0.1:5000/activar/{toke}/{direccion}' aria-pressed="true"> PRESS </a> <br>
                </div>
            </div>
        </div>
    </div>
    </BODY>
</HTML>  
"""
    if valor == 2:
        html = f"""
<HTML>
    <HEAD>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
        <title>RECUPERAR</title>
    </HEAD>
    <BODY style=" background-color: powderblue; align-self: baseline; text-align: center;">
        <div class="text-center">
        <div class="card border-primary mb-3 ">
            <div class="card-header ">
                <h1 class="text-center " style="font-family: 'Times New Roman', Times, serif;background-color: DodgerBlue;">RESTABLECER CONTRASEÑA</h1>
                 </div>
            <div class="card-body">
                <figcaption class="blockquote-footer">
                    <h5 class="card-title">Hola -- Bienvenido : <br><cite title="Source Title"> {direccion} </cite><br> </h5>
                </figcaption>
                <p class="card-text" style="border: 1px solid rgb(91, 174, 185);">
                    para poder restablecer la contraseña <br>
                    de inicio de sesion por favor presione el <br>
                    siguiente boton... </p>
                <div class="text-center">
                    <a style="outline: none;text-decoration: none;display: inline-block;width: 19.5%;margin-right: 0.625%;text-align: center;line-height: 3;color: black;background:silver;" class="button btn-primary" href='http://127.0.0.1:5000/restablecer/{toke}' aria-pressed="true"> PRESS </a> <br>
                </div>
            </div>
        </div>
    </div>
    </BODY>
</HTML>  
"""
        
    
    
    
    
    parte_html = MIMEText(html,"html")
    message.attach(parte_html)

    print("SE ESTA ENVIANDO EL CORREO ESPERE ....")

    server = SMTP(settings.SMTP_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.send_message(message)

    server.quit()
    print("se envio el correo")
