

def correo(direccion):
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
    
    message['Subject'] = "CODIGO DE ACTIVACION"
    message['From'] = 'hermelsalazar2020@itp.edu.co'
    message['To'] = direccion

    html = f"""
    
    <HTML>
        <HEAD>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
  
           estiomado {direccion} para poder terminar con la activacion de su correo adecuadamente.
           por favor presione el boton:
           
        </HEAD>
        <BODY>
            <a href="http://127.0.0.1:5000/activar"  class="btn btn-primary" role="button" aria-pressed="true"> ACTIVAR </a>
        </BODY>
    </HTML> 
    """
    
    parte_html = MIMEText(html,"html")
    message.attach(parte_html)

    # yeferlopez09@gmail.com

    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD

    print("SE ESTA ENVIANDO EL CORREO ESPERE ....")

    server = SMTP(settings.SMTP_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.send_message(message)

    server.quit()
    print("se envio el correo")
