'''
Created on 

Course work: 

@author: chaaya

Source: 
'''
# Import necessary modules

from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "abc123@!"

@app.route("/")
def home():
    if 'user' in session:
        name = session['user']
        return {
        "logged in as": name
        }
    
    return {
        "result" : "not logged in"
    }

@app.route("/login", methods=["GET","POST"] )
def login():
    if request.method == "POST":
        session["user"] = request.values.get('user')
        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


if __name__== "__main__":
    app.run( 
        host="0.0.0.0", 
        debug = True, 
        port = 5000
        )