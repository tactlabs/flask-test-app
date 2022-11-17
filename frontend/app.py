'''
Created on Oct 20, 2022

Course work: 

@author: Sivaraam

Source:
    
'''
# Import necessary modules

from flask import Flask, render_template
import json
import business 


app = Flask(__name__)

@app.route('/')
def start():
    random_result = business.random_num()
    return render_template('index.html',result=random_result)
    

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 8000)
    
    