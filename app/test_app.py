import unittest
from app import app  # Import the Flask app from app.py

class FlaskAppTests(unittest.TestCase):
    # This method is executed before every test method
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the app
        self.app.testing = True  # Set testing mode to True for the app

    # Test the 'hello_world' function and the root route '/'
    def test_hello_world(self):
        response = self.app.get('/')  # Simulate a GET request to the root URL
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200 (OK)
        self.assertEqual(response.data.decode('utf-8'), "Hello, World!")  # Verify that the returned text is "Hello, World!"

# Run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()
