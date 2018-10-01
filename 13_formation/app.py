'''
Sophia Xia
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    # prints <Flask 'app'> 
    print(app)
    return render_template("auth.html")

# default method is GET when POST isn't specified
@app.route("/auth", methods=["POST"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    # return "I like watermelon"
    return render_template("success.html", username = request.cookies.get('username'), sub1 = request.method)
    
if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
