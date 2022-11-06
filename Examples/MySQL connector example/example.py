import sys
import mysql.connector
import json

f = open(sys.argv[1])

credentials = json.load(f)

database = mysql.connector.connect(**credentials["database"])
cursor = database.cursor()

cursor.execute("SELECT * FROM test_table;")
for result in cursor:
    print(result)
#cursor.execute("CREATE TABLE test_table (number1 int, number2 int);")
cursor.execute("INSERT INTO test_table (number1, number2) VALUES (1, 2);")
database.commit()

cursor.close()
database.close()
f.close()