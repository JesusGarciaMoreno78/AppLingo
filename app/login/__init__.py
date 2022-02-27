from flask import Blueprint
password = Blueprint('login', __name__, template_folder='templates', static_folder='static')

from . import routes