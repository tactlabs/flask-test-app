'''
Created on 

Course work: 

@author: chaaya

Source: https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread
'''
# Import necessary modules

from flask import Flask, render_template, request, redirect, url_for
import json
import os
import sqlite3

conn = sqlite3.connect("sample.db", check_same_thread=False)

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "mood":"sleepy"
        }

@app.route("/create/table")
def create():
    conn.execute("CREATE TABLE INFO(name varchar(25), song varchar(50), book varchar(50), colour varchar(25));")
    conn.commit()

    return {
        "result": "table created"
    }

@app.route("/insert")
def insert():
    conn.execute("INSERT INTO INFO(name, song, book, colour) values ('Reenu','Perfect','Percy Jackson','blue');")
    conn.commit()

    return {
        "result" : "values entered"
    }

@app.route("/read")
def read():
    info_list = []
    rows = conn.execute("SELECT * FROM INFO;")
    for row in rows:
        info_list=row
    return {
        "result" : info_list    
    }

@app.route("/update")
def update():
    conn.execute("UPDATE INFO SET song='Photograph' WHERE name='Reenu';")
    conn.commit()

    return {
        "result" : "values updated"
    }

@app.route("/delete")
def delete():
    conn.execute("DELETE FROM INFO WHERE name='Reenu';")
    conn.commit()

    return {
        "result" : "values deleted"
    }

@app.route("/delete/table")
def drop():
    conn.execute("DROP TABLE INFO;")
    conn.commit()

    return {
        "result" : "table deleted"
    }



if __name__== "__main__":
    app.run( 
        host="0.0.0.0", 
        debug = True, 
        port = 5000
        )