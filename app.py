from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Everyone,This Is Shrikant Sharma Your Future Devops Engineer !'

@app.route('/health')
def health():
    return 'Server is up and running'
