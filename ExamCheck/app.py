from flask import Flask, request, render_template
import mysql.connector
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    f = open("../CREDENTIALS.json")
    credentials = json.load(f)
    f.close()

    database = mysql.connector.connect(**credentials["database"]) # create database object
    cursor = database.cursor()

    spot_id = request.args.get("spot_id")
    #print(spot_id)

    cursor.execute(f"SELECT * FROM exam_info WHERE room_seat_num={int(spot_id)}")

    dataDict={}
    for result in cursor:
        print(result)
        dataDict[result[1]]={"studentName":result[0],
                            "examName":result[2],
                            "phoneNum":result[3],
                            "examTime":(result[4],result[5]),
                            "item1": result[6],
                            "item2": result[7],
                            "item3": result[8]}

    if request.method == "POST": # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        print(first_name)
        print(last_name)
    return render_template("index.html", data=cursor)




"""cursor.close()
database.close()"""

if __name__ == "__main__":
    app.run()