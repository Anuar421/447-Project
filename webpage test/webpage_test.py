import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for
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



#Test for shading
@app.route('/shading/', methods=['POST'])
def shading():

    print(request.form['data'])
    county = request.form['data']
    date = '2021-03-21'

    try:
        conn = sqlite3.connect("county_cases.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM county_cases WHERE date='"+date+"' AND county='"+county+"' AND state='California'")
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
            cur.execute("SELECT * FROM county_cases WHERE date='"+date+"' AND county='"+county+"' AND state='California'")
            rows = cur.fetchall()
            print(rows)
    else: 
        for row in rows:
            print(row)

    county_cases = rows[0][4]
    county_deaths = rows[0][5]
    if county_cases == None:
        county_cases = 0
    if county_deaths == None:
        county_deaths = 0

    print("county_cases: ",county_cases,"; county_deaths: ",county_deaths)

 


    return redirect(url_for('users', county_cases=county_cases, county_deaths=0, residents_confirmed=0, residents_deaths=0, 
                                staff_confirmed=0, staff_deaths=0))




@app.route('/find-date/', methods=['POST'])
def findDateCounty():
    print(request.form['Date: '])
    date = request.form['Date: ']
    if (date == ''):
        date = '2021-03-21'

    print(request.form['County: '])
    county = request.form['County: ']

    if (county == ''):
        county = request.form['click_Data']

    print(request.form['County: '])

    print(request.form['Prison: '])
    prison = request.form['Prison: ']

    county_cases = 0
    county_deaths = 0
    residents_confirmed = 0
    residents_deaths = 0
    staff_confirmed = 0
    staff_deaths = 0

    print('date:', date)
    print('county:',county)


    if (prison == ''):
        conn = None
        try:
            conn = sqlite3.connect("county_cases.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM county_cases WHERE date='"+date+"' AND county='"+county+"' AND state='California'")
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
                cur.execute("SELECT * FROM county_cases WHERE date='"+date+"' AND county='"+county+"' AND state='California'")
                rows = cur.fetchall()
                print(rows)
        else: 
            for row in rows:
                print(row)

        county_cases = rows[0][4]
        county_deaths = rows[0][5]
        if county_cases == None:
            county_cases = 0
        if county_deaths == None:
            county_deaths = 0

        print("county_cases: ",county_cases,"; county_deaths: ",county_deaths)

        #return render_template('homepage.html', county_cases=county_cases, county_deaths=county_deaths)
        return redirect(url_for('users', county_cases=county_cases, county_deaths=county_deaths, residents_confirmed=residents_confirmed, residents_deaths=residents_deaths, 
                                staff_confirmed=staff_confirmed, staff_deaths=staff_deaths))
    else:
        conn = None
        try:
            conn = sqlite3.connect("prison_cases.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM prison_cases WHERE Date='"+date+"' AND Name='"+prison+"'")
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
                cur.execute("SELECT * FROM prison_cases WHERE Date='"+date+"' AND Name='"+prison+"'")
                rows = cur.fetchall()
                print(rows)
        else: 
            for row in rows:
                print(row)

        residents_confirmed = rows[0][6]
        staff_confirmed = rows[0][7]
        residents_deaths = rows[0][8]
        staff_deaths = rows[0][9]
        if residents_confirmed == None:
            residents_confirmed=0
        if staff_confirmed == None:
            staff_confirmed=0
        if residents_deaths == None:
            residents_deaths=0
        if staff_deaths == None:
            staff_deaths=0
        print("residents_confirmed:", residents_confirmed," staff_confirmed:",staff_confirmed,"residents_deaths",residents_deaths,"staff_deaths:",staff_deaths)
        #return render_template('homepage.html', county_cases=county_cases, county_deaths=county_deaths)
        return redirect(url_for('users', county_cases=county_cases, county_deaths=county_deaths, residents_confirmed=residents_confirmed, residents_deaths=residents_deaths, 
                                staff_confirmed=staff_confirmed, staff_deaths=staff_deaths))

@app.route('/find-date-prison', methods=['POST'])
def findDatePrison():
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def users():
    try:
        return render_template('homepage.html', county_cases = request.args.get('county_cases'), county_deaths = request.args.get('county_deaths'), residents_confirmed = request.args.get('residents_confirmed'), 
                               residents_deaths = request.args.get('residents_deaths'), staff_confirmed = request.args.get('staff_confirmed'), staff_deaths = request.args.get('staff_deaths'))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run()