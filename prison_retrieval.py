import sqlite3

"""
This is a test program designed to retrieve all elements from prison_cases.db and print them on screen.
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
    cur.execute("SELECT * FROM prison_cases")

    rows = cur.fetchall()
    for row in rows:
        print(row)

"""
Date storage in SQLite is evil. The date 3/14/2021 becomes 2021-03-14
"""
def select_elements_by_date(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM prison_cases WHERE date = '2021-03-14'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    print("in main")
    database = "prison_cases.db"

    conn = create_connection(database)
    with conn:
        #print("Querying all elements")
        #select_all_elements(conn)
        print("Obtaining case data where date = 3/14/2021")
        select_elements_by_date(conn)