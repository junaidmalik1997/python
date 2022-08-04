from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world3333334444444444444'

app.run(host='0.0.0.0', port=82)
