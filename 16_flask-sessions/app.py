'''
CAD - Caden, Aditya, Danny
SoftDev
K16 - Flask-Sessions - Using Flask and cookies
2024 - 10 - 09
Time Spent:  
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

from key import pkey


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = pkey 

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]
    return render_template('response.html', username = session["username"]) #response to a form submission

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop("username")
    session.pop("password")
    return render_template('logout.html')

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
