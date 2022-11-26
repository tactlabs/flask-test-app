'''
Created on 

Course work: 

@author: chaaya

Source: https://www.askpython.com/python-modules/flask/flask-redirect-url
        https://stackoverflow.com/questions/61040047/how-to-pass-arguments-for-return-redirecturl-in-flask
    
'''
# Import necessary modules

from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def start():
    result = {
        "chaaya" : "the great"
    }

    return result


# @app.route('/get/info',methods=["GET", "POST"])
# def get_info():
#     # if request.method == 'GET':
#     name = request.values.get('name')
#     colour = request.values.get('colour')

#         # return redirect(url_for("random_func", name=name, colour= colour))

#     return render_template("index.html",name=name, colour= colour)

@app.route('/get/info',methods=["GET", "POST"])
def get_info():
    if request.method == 'POST':
        name = request.form['name']
        colour = request.form['colour']
        return redirect(f"/jaffi/{name}/{colour}")

    return render_template("index.html")
    

# @app.route('/jaffi/<name>/<colour>')
# def random_func(name,colour):
#     # name = request.args.get('name')
#     # colour=request.args.get('colour')
#     result = {
#         "name" : name,
#         "favorite colour" : colour
#     }

    return  result
if __name__== "__main__":
    app.run( 
        host="0.0.0.0", 
        debug = True, 
        port = 5000
        )