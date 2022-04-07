

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