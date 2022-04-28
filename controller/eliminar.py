from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import archivo


def eliminararchivo(id):
    archivo.eliminararchivo(id=id)
    archivos = archivo.obtenerarchivo(id=session["usuario_id"])
    return archivos