from multiprocessing import Process

server = Process(target=my-app.run)
server.start()
# ...
server.terminate()
server.join()


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

app.run(host='0.0.0.0', port=82)
