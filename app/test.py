#! /usr/bin/env python3 
import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        return "Nothing to post!\n"
    else:
        return "Hello World!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

