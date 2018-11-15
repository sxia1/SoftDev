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

@app.route("/cat_facts")
def hello_world:
    return render_template('catFacts.html')

@app.route("/studio_ghibli")
def hello_world:
    return render_template('studioGhibli.html')

@app.route("/sunset_rise")
def hello_world:
    return render_template('sunsetRise.html')


if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
