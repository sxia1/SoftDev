from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
req = urllib.request.urlopen(url)
data = req.read()
encoding = req.info().get_content_charset('utf-8')
dict = json.loads(data.decode(encoding))

@app.route("/")
def home():
    return render_template('index.html', INFO = dict.values())

if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
