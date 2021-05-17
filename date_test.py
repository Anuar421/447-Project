
import sqlite3
import datetime

"""
This is a test program intended to implement next-closest-date functionality.
"""



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_elements_by_date(conn, date):
    cur = conn.cursor()
    cur.execute("SELECT * FROM county_cases WHERE date='"+date+"'")
    rows = cur.fetchall()

    if not rows:
        print("Invalid date; moving to closest earliest date.")
        

        today = datetime.datetime.now()
        #if the current date isnt there subract one until there is
        #while not rows:
        for x in range(3):
            today -= datetime.timedelta(days=1)
        date = today.strftime("%Y-%m-%d")


        print(date)
        cur.execute("SELECT * FROM county_cases WHERE date='"+date+"'")
        rows = cur.fetchall()
        print(rows)
    else: 
        for row in rows:
            print(type(row))
        
if __name__ == '__main__':
    database = "county_cases.db"
    conn = create_connection(database)
    date = input("Enter your desired date (year-month-date format)")
    select_elements_by_date(conn, date)