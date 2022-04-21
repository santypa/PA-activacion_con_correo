
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
    from controller import token
    
    url =token.acortarPost()
    print(url)
    
    message = EmailMessage()
    message = MIMEMultipart("alternative")
    
    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD
    
    message['Subject'] = "CODIGO DE ACTIVACION"
    message['From'] = username
    message['To'] = direccion

    html = f"""
    
    <HTML>
        <HEAD>
           estiomado {direccion} para poder terminar con la activacion de su correo adecuadamente.
           por favor presione el boton:
        </HEAD>
        <BODY>
            <a  href='http://127.0.0.1:5000/activar/{url}/{direccion}' aria-pressed="true"> ACTIVAR </a>
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
