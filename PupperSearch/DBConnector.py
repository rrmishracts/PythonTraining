#!/usr/bin/python

import mysql.connector
import day2_model as model

def connect():
	# Open database connection
	db = mysql.connector.connect(user="root",password="root",host="127.0.0.1", database="pythonTest" )
	return db
	

def readbreed(read_sql):
	db = connect()
	cursor = db.cursor()
	#sql1 = "select * from pythontest.breed"
	cursor.execute(read_sql)
	for x in cursor:
	  print(x)
	  
	# disconnect from server
	db.close()

	
def writebreed(write_sql):
	db = connect()
	cursor = db.cursor()
	cursor.execute(write_sql)
	db.commit()	
	
	# disconnect from server
	db.close()


def readpupper(read_sql):
	db = connect()
	cursor = db.cursor()
	#sql1 = "select * from pythontest.pupper;"
	cursor.execute(read_sql)
	for x in cursor:
	  print(x)
	  
	# disconnect from server
	db.close()

	
def writepupper(write_sql):
	print("Inside writepupper method")
	db = connect()
	cursor = db.cursor()
	cursor.execute(write_sql)
	db.commit()
	
	# disconnect from server
	db.close()

	
#Create Table already covered through mysql workbench
#sql1="DROP TABLE IF EXISTS pythontest.pupper"
#sql2="DROP TABLE IF EXISTS pythontest.breed"

#cursor.execute("select * from pythontest.PUPPER")
#for x in cursor:
#  print(x)


sql1 = "INSERT INTO pythontest.breed (name, temperament, coat) VALUES ('Boxer', 'Alert, patient, playful, wary of strangers', 'Short, shiny, smooth, and tight');"
sql2 = "INSERT INTO pythontest.breed (name, temperament, coat) VALUES ('Bichon Frise', 'Cheerful, gentle, affectionate', 'Soft undercoat; coarse, curley outercoat');"
sql3 = "INSERT INTO pythontest.breed (name, temperament, coat) VALUES ('Siberian Husky', 'Friendly, gentle, alert, outgoing', 'Double, medium length');"

sql4 = "INSERT INTO pythontest.PUPPER (name, sex, weight, height, color, date_of_birth, breed_id) VALUES ('Lexi', 'F', 58, 22, 'Brown with Black', '20130418', 1);"
sql5 = ""
sql6 = ""
sql7 = ""
sql8 = ""

#writebreed(sql1)
#writebreed(sql2)
#writebreed(sql3)

writepupper(sql4)
#writepupper(sql5)
#writepupper(sql6)
#writepupper(sql7)
#writepupper(sql8)


print("Function End")
