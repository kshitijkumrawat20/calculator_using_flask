from flask import Flask
from flask import request 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" 

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>" 

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>" 

@app.route("/test2")
def test():
    data = request.args.get('x')
    return f"this is data input drom my url{data}"



if __name__ == "__main__":
    app.run(host="0.0.0.0")  