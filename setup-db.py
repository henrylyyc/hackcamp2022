import mysql.connector
import json

f = open("CREDENTIALS.json")

credentials = json.load(f)

database = mysql.connector.connect(**credentials["database"]) # create database object
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS exam_info (\
    name varchar(255),\
    student_num int,\
    exam_name varchar(255),\
    instructor_contact varchar(255),\
    exam_start datetime,\
    exam_duration float,\
    last_time_checked datetime,\
    needs_help boolean,\
    started boolean,\
    room_seat_num varchar(255)\
    )")

cursor.execute("SHOW TABLES")
for result in cursor:
    print(result)

print()
cursor.execute("DESCRIBE exam_info")
for result in cursor:
    print(result)
#cursor.execute("DROP TABLE exam_info")

cursor.close()
database.close()
f.close()