import sqlite3

"""
This is a test program designed to retrieve all elements from county_cases.db and print them on screen.
"""

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_elements(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM county_cases")

    rows = cur.fetchall()
    for row in rows:
        print(row)

"""
Date storage in SQLite is evil. The date 2/4/2020 becomes 2020-02-04
"""
def select_elements_by_date(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM county_cases WHERE date = '2020-02-04'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    print("in main")
    database = "county_cases.db"

    conn = create_connection(database)
    with conn:
        #print("Querying all elements")
        #select_all_elements(conn)
        print("Obtaining case data where date = 2/4/2020")
        select_elements_by_date(conn)