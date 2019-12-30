# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    #return render_template("index.html")
    str = "<h1 style='color:blue'>Hello World!!</h1><br />"
    str += "すいません、ちょっと通りますよ・・・<br /><br />"
    str += "　　　／⌒ヽ<br />"
    str += "　　/　´_ゝ`）<br />"
    str += "　　|　 　　/<br />"
    str += "　　| /|　|<br />"
    str += "　 //　| |<br />"
    str += "　Ｕ　 .Ｕ<br />"
    return str

if __name__ == "__main__":
    app.run(host='0.0.0.0')
