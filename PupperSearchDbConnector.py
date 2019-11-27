import pymysql
import sys

db = pymysql.connect("localhost", "root", "root", "sample_schema")

cursor = db.cursor()

sql = """INSERT INTO breed (name, temperament, coat) 
VALUES ('Boxer', 'Alert, patient, playful, wary of strangers', 'Short, shiny, smooth, and tight')"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

db.close()
'''
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM sample_schema.test_table"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      gender = row[2]
      # Now print fetched result
      print ("id = %d,name = %s,gender = %s" % (id, name, gender))


except:
   print("Unexpected error:", sys.exc_info())

   # disconnect from server

'''
