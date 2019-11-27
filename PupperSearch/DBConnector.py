#!/usr/bin/python

import mysql.connector


def connect():
	# Open database connection
	db = mysql.connector.connect(user="root",password="root",host="127.0.0.1", database="pythonTest" )
	return db
	

def readBreed(read_sql,idList):
	db = connect()
	cursor = db.cursor()
	cursor.execute(read_sql,idList)
	for x in cursor:
	  print(x)
	  
	# disconnect from server
	db.close()

	
def writeBreed(write_sql,data):
	db = connect()
	cursor = db.cursor()
	cursor.execute(write_sql,data)
	db.commit()	
	
	# disconnect from server
	db.close()


def readPupper(read_sql,idList):
	db = connect()
	cursor = db.cursor()
	cursor.execute(read_sql,idList)
	for x in cursor:
	  print(x)
	  
	# disconnect from server
	db.close()

	
def writepupper(write_sql, data):
	print("Inside writepupper method")
	db = connect()
	cursor = db.cursor()
	cursor.execute(write_sql, data)
	db.commit()
	
	# disconnect from server
	db.close()
