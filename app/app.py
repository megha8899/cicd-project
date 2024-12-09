from flask import Flask
import os  # Import the os module

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


