#Sophia Xia
#SoftDev1 pd6
#K8 -- Fill Yer Flask
#2018-09-18

'''
Notes:
print statements appear in the terminal
String returned by function shows up on the webpage
type in the route after the / to get other pages to show up
MUST lead with a slash, shows error in terminal and crashes
print statements in the fxn that follows the route will print in the terminal
once the route is opened
perhaps the print statements are just for debugging purposes?
In debugging mode, no need to close and open again to see changes and the change
will be reflected by a mssg in the terminal once the changes are saved
__name__ and __main__ are most likely naming conventions?
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__) # where will this go?
    return "No hablo queso!"

@app.route("/me")
def about():
    print("about to print __name__...")
    print(__name__)
    return "Hi, I'm an alien!"

@app.route("/nom")
def favorite():
    print("about to print __name__...")
    print(__name__)
    return "I enjoy eating savory foods!"

if __name__ == "__main__":
    app.debug = True
    app.run()

app.debug = True
app.run()
