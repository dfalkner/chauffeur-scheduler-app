# chauffer-scheduler-app/modules/owner/views.py
# Owner views for Chauffeur Scheduler App

from flask import Blueprint

owner_blueprint = Blueprint('owner', __name__)


@owner_blueprint.route('/dashboard')
def dashboard():
    return "Owner Dashboard"