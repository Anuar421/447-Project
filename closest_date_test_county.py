import sqlite3

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
            print(type(row))
        
if __name__ == '__main__':
    database = "county_cases.db"
    conn = create_connection(database)
    date = input("Enter your desired date (year-month-date format)")
    select_elements_by_date(conn, date)