import sqlite3
import pandas as pd

if __name__ == '__main__':
    conn = sqlite3.connect('prison_cases.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE prison_cases ("Facility.ID" int, Jurisdiction text, State text, Name text, Date text, source text, "Residents.Confirmed" int, "Staff.Confirmed" int, "Residents.Deaths" int, "Staff.Deaths" int, 
    "Residents.Recovered" int, "Staff.Recovered" int, "Residents.Tadmin" int, "Staff.Tested" int, "Residents.Negative" int, "Staff.Negative" int, "Residents.Pending" int, "Staff.Pending" int, "Residents.Quarantine" int, 
    "Staff.Quarantine" int, "Residents.Active" int, "Population.Feb20" int, "Residents.Population" int, "Residents.Tested" int, "Residents.Initiated" int, "Residents.Completed" int, "Residents.Vadmin" int, "Staff.Initiated" int, 
    "Staff.Completed" int, "Staff.Vadmin" int, Address text, Zipcode int, City text, County text, Latitude real, Longitude real, "County.FIPS" int, "HIFLD.ID" int, jurisdiction_scraper text, Description text, Security text, 
    Age text, Gender text, "Is.Different.Operator" text, "Different.Operator" text, Capacity int, "BJS.ID" text, "Source.Population.Feb20" text, "Source.Capacity" text, Website text, 
    "ICE.Field.Office" text)''')

    cases = pd.read_csv('CA-historical-data.csv')
    cases.to_sql('prison_cases', conn, if_exists='append', index = False)

    c.execute('''SELECT * FROM prison_cases''').fetchall()