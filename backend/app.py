'''
Created on Oct 20, 2022

Course work: 

@author: Sivaraam

Source:
    
'''
# Import necessary modules

from flask import Flask
import json
import business
import os


app = Flask(__name__)

FLASK_BACKEND_PORT = os.environ.get('FLASK_BACKEND_PORT')


@app.route('/')
def start():
    random_result = business.random_num()
    result_dict={
        'random_number':random_result
        }

    return result_dict
    

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = FLASK_BACKEND_PORT
    )
    
    