'''
Sophia Xia
SoftDev1 pd6
K --
2018-11-
'''

import json

from flask import Flask, render_template

from urllib import request

app = Flask(__name__)

@app.route("/")
def hello_world:
    return render_template('temp.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
