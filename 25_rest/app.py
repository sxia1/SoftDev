'''
Sophia Xia
SoftDev1 pd6
K25 -- Getting More REST
2018-11-14
'''

from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def home():
    url = "https://data.cityofnewyork.us/resource/waf7-5gvc.json"
    req = urllib.request.urlopen(url)
    data = req.read()
    dict = json.loads(data)
    for each in dict:
        print(each.values())
    return render_template('index.html', INFO = dict)

if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
