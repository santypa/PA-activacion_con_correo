

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from msilib.schema import MIME


def correo(asunto,direccion):
    from flask import request
    from config import settings
    from email import message
    from http import server
    from cgitb import html
    from smtplib import SMTP
    from email.message import EmailMessage
    from typing_extensions import Required
   
    
    message = EmailMessage()

    message['Subject'] = asunto
    message['From']='hermelsalazar2020@itp.edu.co'
    message['To']= direccion
    ''' message = MIMEMultipart()
    
    html_body = f
    <html>
        <header></header>
        <body>
        
        <h1>BIENVENIDO</h1>
        <p>
        para verificar su correo presione el siguiente boton 
        gracias
        </p>
        
            hola mundo
        </body>
    </html>
    
   
    message.attach(MIMEText(html_body,"html")) '''
    
    #yeferlopez09@gmail.com

    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD

    print("SE ESTA ENVIANDO EL CORREO ESPERE ....")

    server = SMTP(settings.SMTP_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.send_message(message)

    server.quit() 
    print("se envio el correo")