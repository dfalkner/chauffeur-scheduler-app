# tests/test_app.py
import unittest
from app import create_app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client using the Flask application configured for testing
        self.app = create_app({'TESTING': True})
        self.client = self.app.test_client()

    def test_hello_endpoint(self):
        # Test the /hello endpoint
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, World!')

    def test_index_endpoint(self):
        # Test the index endpoint
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Chauffeur Scheduler App!', response.data.decode())

    def test_dashboard_endpoint(self):
        # Test the /dashboard endpoint
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        # Replace 'Dashboard Page' with the actual content you expect from the dashboard page
        self.assertIn('Dashboard Page', response.data.decode())

        # Run the tests if the file is executed directly


if __name__ == '__main__':
    unittest.main()