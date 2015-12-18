from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail
from flask.ext.mail import Message
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)
data = {}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/exploreitaly')
def exploreitaly():
    return render_template('exploreitaly.html')

@app.route('/exploreusa')
def exploreusa():
    return render_template('exploreusa.html')

@app.route('/exploretaiwan')
def exploretaiwan():
    return render_template('exploretaiwan.html')

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

application = app
