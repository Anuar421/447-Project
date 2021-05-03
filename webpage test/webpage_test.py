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


@app.route('/find-date/', methods=['POST'])
def findDate():
    print(request.form['Date: '])
    date = request.form['Date: ']

    conn = None
    try:
        conn = sqlite3.connect("county_cases.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM county_cases WHERE date='"+date+"'")
    rows = cur.fetchall()
    if not rows:
        print("Invalid date; moving to closest earliest date.")
        while not rows:
            array = date.split('-')
            array[1] = array[1].lstrip('0')
            array[2] = array[2].lstrip('0')
            print(array)
            if int(array[2]) > 1:
                array[2] = int(array[2]) - 1
            elif int(array[1]) > 1:
                array[2] = 31
                array[1] = int(array[1]) - 1
            else :
                array[0] = int(array[0]) - 1
                array[1] = 12
                array[2] = 31

            if int(array[1]) < 10:
                date = str(array[0])+"-0"+str(array[1])
            else:
                date = str(array[0])+"-"+str(array[1])

            if int(array[2]) < 10:
                date = date+"-0"+str(array[2])
            else:
                date = date+"-"+str(array[2])

            print(date)
            cur.execute("SELECT * FROM county_cases WHERE date='"+date+"'")
            rows = cur.fetchall()
            print(rows)
    else: 
        for row in rows:
            print(row)

    return redirect('/')

@app.route('/')
def users():
    try:
        return render_template('homepage.html')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run()