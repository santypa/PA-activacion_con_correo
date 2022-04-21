from sqlalchemy import false
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash,session
import string
import random

def acortarPost():
    
    for x in range(5):
        code= (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
    forma = code
    
    return forma

