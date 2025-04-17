from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Simple Flask application'

if __name__ == '__main__':
    # This ensures the app runs on 0.0.0.0 so Docker can expose it
    app.run(host='0.0.0.0', port=5000)
