'''
Sophia Xia
SoftDev1 pd6
K26 -- Getting More REST
2018-11-15
'''

import json

from flask import Flask, render_template

import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cat")
def cat():
    breed = "https://catfact.ninja/breeds?limit=5"
    req = urllib.request.urlopen(breed)
    data = req.read()
    dictB = json.loads(data)
    
    fact = "https://catfact.ninja/fact"
    req = urllib.request.urlopen(fact)
    data = req.read()
    dictF = json.loads(data)
    
    facts = "https://catfact.ninja/facts?limit=2"
    req = urllib.request.urlopen(facts)
    data = req.read()
    dictFS = json.loads(data)
    return render_template('cat.html', BINFO = dictB['data'], FINFO = dictF, FSINFO = dictFS['data'])

@app.route("/ghibli")
def ghibli():
    url = "https://ghibliapi.herokuapp.com/films"
    req = urllib.request.urlopen(url)
    data = req.read()
    dict = json.loads(data)

    return render_template('ghibli.html', FILMS = dict)

@app.route("/sun")
def sunset():
    lat = "lat=40.783058"
    lng = "&lng=-73.971252"
    date = "&date=2018-11-01"
    url = "https://api.sunrise-sunset.org/json?" + lat + lng + date
    req = urllib.request.urlopen(url)
    data = req.read()
    dict = json.loads(data)
    return render_template('sun.html', SUN = dict['results'])


if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
