# chauffer-scheduler-app/modules/scheduler/views.py
# Scheduler views for Chauffeur Scheduler App

from flask import Blueprint

scheduler_blueprint = Blueprint('scheduler', __name__)


@scheduler_blueprint.route('/schedule')
def schedule():
    return "Scheduler Page"