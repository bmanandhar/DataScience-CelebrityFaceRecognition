#http://127.0.0.1:5000/hello
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world."

if __name__=="__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()