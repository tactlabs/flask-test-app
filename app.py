'''
Created on 

Course work: 

@author: Vedha

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
    app.run(debug=True)