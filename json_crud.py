'''
Created on 

Course work: 

@author: chaaya

Source: 
'''
# Import necessary modules

from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

FILE_NAME = "test.json"

@app.route("/")
def home():
    return {
        "mood":"sleepy"
        }

@app.route("/create/file")
def create():
    try:
        f = open(FILE_NAME,"x")
        f.write("{}")
        msg = "File created"
    except Exception as e:
        msg = str(e)
    
    return {
        "result" : msg
    }

@app.route("/write")
def write():
    dict1 = {
        "name" : "Reenu", 
        "colour" : "Blue",
        "song" : "Perfect by Ed Sheeran"
    }

    data = json.dumps(dict1,indent=5)
    f = open(FILE_NAME,"w")
    f.write(data)

    return dict1

@app.route("/read")
def read():
    f = open("test.json","r")
    data = json.load(f)

    return data

@app.route("/update",methods=['GET','POST'])
def update():
    if request.method == "POST":
        f = open("test.json","r")
        data = json.load(f)
        # data['book'] = "Percy Jackson"
        name = request.values.get("name")
        colour = request.values.get("colour")
        book = request.values.get("book")
        song = request.values.get("song")

        data[name] = {
            "fav_song": song,
            "fav_colour" : colour,
            "fav_book" : book
        }
        
        f.close()
        f1=open("test.json","w")
        data1 = json.dumps(data,indent=5)
        f1.write(data1)

    return render_template("get_info.html")

@app.route("/delete/file")
def delete():
    os.remove(FILE_NAME)

    return {
        "result" : "File deleted"
    }


if __name__== "__main__":
    app.run( 
        host="0.0.0.0", 
        debug = True, 
        port = 5000
        )