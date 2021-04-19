import sqlite3

from flask import Flask, render_template, request, flash, redirect
from tables import Results
app = Flask(__name__)
app.secret_key = "secret key"

"""
Vomit out SQLite data onto a webpage?
"""

@app.route('/map.js')
def map():
    return render_template('map.js')

@app.route('/CA/counties.js')
def counties():
    return render_template('CA/counties.js')

@app.route('/')
def users():
    try:
        return render_template('homepage.html')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run()