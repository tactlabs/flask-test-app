'''
Created on Oct 20, 2022

Course work: 

@author: Sivaraam

Source:
    
'''
# Import necessary modules

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def start():

    return render_template('index.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 8000)