import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from flask import Flask, template_rendered
from contextlib import contextmanager
from modules.auth.views import auth_blueprint
from unittest.mock import patch

import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
from modules.owner.views import owner_blueprint
app.register_blueprint(owner_blueprint, url_prefix='/owner')

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_get(self):
        with captured_templates(app) as templates:
            response = self.app.get('/auth/login')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'login.html')

    def test_login_post(self):
        # This test will need to be expanded with logic to mock AWS Cognito authentication
        response = self.app.post('/auth/login', data=dict(
            username='testuser',
            password='testpass'
        ))
        # Check for redirection (302) to the owner dashboard
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/owner/dashboard' in response.headers['Location'])

    def test_login_post_failure(self):
        with captured_templates(app) as templates:
            response = self.app.post('/auth/login', data=dict(
                username='wronguser',
                password='wrongpass'
            ))
            # Assuming the application redirects to the login page on failure
            self.assertEqual(response.status_code, 302)
            # Check that the Location header is set to the login page (without an error message)
            self.assertTrue('/auth/login' in response.headers['Location'])
            # Optionally, if the application uses flash messages or similar, check for that instead
            # self.assertIn('error', response.data.decode())

if __name__ == '__main__':
    unittest.main()
