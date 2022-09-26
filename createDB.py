import sqlite3 # note, sqlite3 comes with python3

##### Note, this is just an example script, to create a database, you need to do this manually.
## otherwise you just need to run this once and then you can use the database in your flask app

### For a brief tutorial on sqlite using pythong, please visit: https://www.tutorialspoint.com/sqlite/sqlite_python.htm 
### You can scroll down to where it says 'Connect To Database' 
### For an additional tutorial that goes through the basics, please see: https://www.sqlitetutorial.net/sqlite-python/ 

# Connecting to sqlite
# connection object
connect = sqlite3.connect('./flask-with-db/patients.db')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# // commit () --> This method commits the current transaction. If you don't call this method, 
# anything you did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL,
            zipcode CHAR(25) NOT NULL,
            lengthofstay CHAR(25) NOT NULL,
            icd10code CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes, this is annoying but necessary


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('12345', 'John', 'Smith', '01/01/2000', 'Humana', '19876', '5', '118.79')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('23456', 'Jane', 'Doe', '02/02/2001', 'Aetna', '97585', '6',  '78.6')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('34567', 'Mary', 'Smith', '03/03/2002', 'Cigna', '98765', '7', '99.2')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('45678', 'Bob', 'Smith', '04/04/2003', 'UnitedHealthCare', '87654', '8', '106.42')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('56789', 'Jane', 'Doe', '05/05/2004', 'Medicare', '76543', '9', '70.6' )")

#dummyPerson6 = """ INSERT INTO patient_table(mrn, firstname, lastname, dob, insurance, zipcode, lengthofstay, icd10code) values('32323', 'John321', 'Smith123', '01/01/2000', 'Medicaid', '65432', '4', '61.42' ) """
#db.execute(dummyPerson6)

connect.commit()


# close the connection
connect.close()