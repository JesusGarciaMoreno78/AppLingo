from flask import render_template, request, redirect, url_for

import app
from . import password
from .models import Usuario
from .forms import UsuarioForm, LoginForm
from .auxiliar import encriptar_password, desencriptar_password
from .. import db

PEEPER = "ClaveSecretaPeeper"


@password.route('/')
def index():  # put application's code here
    return render_template('index.html')

@password.route("/welcome/")
def welcome():
    return render_template("welcome.html")

@password.route("/hasheadapeeper/", methods=["GET","POST"])
def hasheadapeeper():
    error = ""
    form = UsuarioForm(request.form)
    return render_template("hasheadapeeper.html", form=form, error=error)

@password.route("/loginhasheadopeeper/", methods=["GET","POST"])
def loginhasheadopeeper():
    error = ""
    form = LoginForm(request.form)
    return render_template("loginhasheadopeeper.html", form=form, error=error)
