# app.py
from flask import Flask
import os


def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

        # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'Welcome to the Chauffeur Scheduler App!'

    @app.route('/dashboard')
    def dashboard():
        return 'Dashboard Page'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

        # Register blueprints and other app configurations here

    # ...

    return app


# Later on, you can create an app instance for running like this:
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)