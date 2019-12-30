# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str = "<h1 style='color:blue'>Hello There!</h1>"
    str += "こんにちは。眠いです。<p />"
    str += "2019/12/30<br />"
    str += "PM 24:00<br />"
    return str

if __name__ == "__main__":
    app.run(host='0.0.0.0')
