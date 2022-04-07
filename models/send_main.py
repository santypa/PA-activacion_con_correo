from cgitb import html
from email import message
from http import server
from smtplib import SMTP
from email.message import EmailMessage
from typing_extensions import Required

from flask import request
from config import settings

message = EmailMessage()

message['Subject'] = "ESTE es el asunto"
message['From']='hermelsalazar2020@itp.edu.co'
message['To']='yeferlopez09@gmail.com'
message.set_content(request("login.html"))


username = settings.SMTP_USERNAME
password = settings.SMTP_PASSWORD

print("SE ESTA ENVIANDO EL CORREO ESPERE ....")

server = SMTP(settings.SMTP_HOSTNAME)
server.starttls()
server.login(username, password)
server.send_message(message)

server.quit() 