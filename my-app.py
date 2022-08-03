# from multiprocessing import Process

# server = Process(target=app.run)
# server.start()
# # ...
# server.terminate()
# server.join()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world2'

app.run(host='0.0.0.0', port=82)
