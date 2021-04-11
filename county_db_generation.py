import sqlite3
import pandas as pd

if __name__ == '__main__':
    conn = sqlite3.connect('county_cases.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE county_cases (date text, county text, state text, fips int, cases int, deaths int)''')

    cases = pd.read_csv('us-counties.csv')
    cases.to_sql('county_cases', conn, if_exists='append', index = False)

    c.execute('''SELECT * FROM county_cases''').fetchall()