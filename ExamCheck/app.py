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
    print(spot_id)

    cursor.execute(f"SELECT * FROM exam-data WHERE room_seat_num={int(spot_id)}")
    for result in cursor:
        print(result)

    if request.method == "POST": # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        print(first_name)
        print(last_name)
    return render_template("index.html")

"""cursor.close()
database.close()"""

if __name__ == "__main__":
    app.run()