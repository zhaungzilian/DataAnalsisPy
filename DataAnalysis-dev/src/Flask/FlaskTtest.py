from flask import Flask
from gevent import pywsgi

app = Flask(__name__)

@app.route('/')
def index():
 return "hello flask!"


server = pywsgi.WSGIServer(('127.0.0.1', 8080), app)
server.serve_forever()


if __name__=='__main__':
    app.run()