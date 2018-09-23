'''Daniel Gelfand and Sophia Xia
SoftDev1 pd<6>
K<10> -- Jinja Tuning
2018-09-24'''

from random import randint
import csv #import csv module
from flask import Flask, render_template

with open('occupations.csv','r') as csvfile: #opens occupations.csv as a readable file saved as variable csvfile
    csvreader = csv.reader(csvfile) #reads the whole file
    next(csvreader) # doesn't read the header
    dict = {rows[0]:float(rows[1]) for rows in csvreader} #creates a dictionary where every even row is a key and every odd is a value
    dict.pop('Total') # removes the Total key from dict

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print(__name__)
    return render_template('test.html', collection = dict, theOne = randint(1,998), ctr = 0)

@app.route("/stuy")
def hello_stuy():
    return "GO STUY!"

if __name__ == "__main__":
    app.debug = True
    app.run()
