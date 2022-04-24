from flask import Flask, render_template, request, redirect, url_for, flash, session
from email.mime import image
from requests import session
from config.database import db


def sesion():
    if  session["usuario_id"] != None:
        return render_template("archivos.html")
    return