from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.nasa.gov/planetary/apod?api_key=zIOpt7HlAwHA2rs8CiUZvnRSUeA32xoMGsWMewtA"
    req = urllib.request.urlopen(url)
    data = req.read()
    encoding = req.info().get_content_charset('utf-8')
    dict = json.loads(data.decode(encoding))
    return render_template('index.html', INFO = dict)

if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
