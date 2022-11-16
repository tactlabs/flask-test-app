'''
Created on Oct 20, 2022

Course work: 

@author: Sivaraam

Source:
    
'''
# Import necessary modules

from flask import Flask, render_template
import json
import random

app = Flask(__name__)

@app.route('/')
def start():
    random_num()
    random_result = random_num()
    return render_template('index.html',result=random_result)

    

def random_num():
    random_number=random.randint(0,100)
    return random_number

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 8000)
    
    