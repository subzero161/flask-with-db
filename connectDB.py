import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('flask-with-db\patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# save the data to a dataframe
df = pd.DataFrame(patientListSql)
df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'insurance', 'zipcode', 'lengthofstay', 'icd10code']
df