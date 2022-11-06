import sys
import mysql.connector
import json

# run with: python example.py path/to/CREDENTIALS.json
# See Slack chat for what's in CREDENTIALS.json

f = open(sys.argv[1]) # open credentials file

credentials = json.load(f) # turn credentials JSON file into a dictionary

database = mysql.connector.connect(**credentials["database"]) # create database object
cursor = database.cursor()

cursor.execute("SELECT * FROM test_table;") # get everything in test_table
for result in cursor:
    print(result)
#cursor.execute("CREATE TABLE test_table (number1 int, number2 int);") # create a new table called test_table
cursor.execute("INSERT INTO test_table (number1, number2) VALUES (1, 2);") # put a value into test_table
database.commit()

cursor.close()
database.close()
f.close()