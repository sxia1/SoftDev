'''

Sophia Xia
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)

user = "JAMIIII";
pswd = "swordfish";

@app.route("/")
def home():
    # prints <Flask 'app'> 
    print(app)
    return render_template("auth.html")

# default method is GET when POST isn't specified
@app.route("/usrfail")
def wrongusr():
    return render_template("auth.html", ERROR = "SHAME ON YOU, WRONG USERNAME")

@app.route("/auth", methods=["POST"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.cookies.get('username'))
    print(request.headers)
    # return "I like watermelon"
    usr = request.cookies.get('username')
    password = request.cookies.get('password')
    if username != user:
        print(request.cookies.get('username'))
        return redirect(url_for("wrongusr"))
    return render_template("welcome.html", username = usr, password = password, sub1 = request.method)
    
if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
