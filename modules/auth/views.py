# chauffer-scheduler-app/modules/auth/views.py
# Authentication views for Chauffeur Scheduler App

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login')
def login():
    return "Login Page"