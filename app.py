# app.py
from flask import Flask
from vedantPackage import greet  # Use underscore instead of hyphen

app = Flask(__name__)

@app.route('/')
def home():
    message = greet()
    return message  # Return the message to display it in the browser

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)