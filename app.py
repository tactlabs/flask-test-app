from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', 'POST'])
def start():

    return render_template('index.html')


if __name__== "__main__":
    app.run(debug=True)