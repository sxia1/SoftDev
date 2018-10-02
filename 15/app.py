'''
JamBuds
Sophia Xia, Mohammed S. Jamil
SoftDev1 pd6
K14 -- Do I Know You?
2018-10-01
'''

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)

user = 'JAMIIII'
pswd = 'swordfish'

@app.route('/')
def home():
    # prints <Flask 'app'> 
    print(app)
    if 'JAMIIII' in session:
        return render_template('welcome.html', username = 'JAMIIII')
    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('JAMIIII')
    return redirect(url_for('home'))

@app.route('/usrfail')
def wrongusr():
    return render_template('auth.html', ERROR = 'SHAME ON YOU, WRONG USERNAME')

@app.route('/pwdfail')
def wrongpwd():
    return render_template('auth.html', ERROR = 'SHAME ON YOU, WRONG PASSWORD')

@app.route('/auth', methods=['GET','POST'])
def authenticate():
    print(request.cookies)

    usr = request.args['username']
    passwd = request.args['password']
    
    #redirects user based on unsuccessful login
    if usr != user:
        return redirect(url_for('wrongusr'))
    elif passwd != pswd:
        return redirect(url_for('wrongpwd'))

    #redirects user to home page if successful
    session[usr] = pswd
    return redirect(url_for('home'))

app.debug = True
app.run()
