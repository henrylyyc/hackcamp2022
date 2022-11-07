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
    if spot_id:
        cursor.execute(f"SELECT * FROM exam_info WHERE room_seat_num={int(spot_id)}")
        
        (name, student_num, exam_name, instructor_contact, exam_start, exam_duration, last_time_checked, needs_help, started, _) = tuple(list(cursor)[0])

        if request.method == "POST": # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
            name = request.form.get("name")
            student_num = request.form.get("student_num")
            exam_name = request.form.get("exam_name")
            instructor_contact = request.form.get("instructor_contact")
            exam_start = request.form.get("exam_start")
            exam_duration = request.form.get("exam_duration")
            last_time_checked = request.form.get("last_time_checked")
            needs_help = request.form.get("needs_help") != None
            started = request.form.get("started") != None

            print(name)
            print(student_num)
            print(exam_name)
            print(instructor_contact)
            print(exam_start)
            print(exam_duration)
            print(last_time_checked)
            print(needs_help)
            print(started)

            cursor.execute(f"DELETE FROM exam_info WHERE spot_id={int(spot_id)}")
            cursor.execute(f"INSERT INTO exam_info VALUES (\"{name}\", {student_num}, \"{exam_name}\", \"{instructor_contact}\", \"{exam_start}\", {exam_duration}, \"{last_time_checked}\", {int(needs_help), int(started)})")

    cursor.close()
    database.close()

    return render_template("index.html", name=name, student_num=student_num, exam_name=exam_name, instructor_contact=instructor_contact, exam_start=exam_start, exam_duration=exam_duration, last_time_checked=last_time_checked, needs_help=bool(needs_help), started=bool(started))

if __name__ == "__main__":
    app.run()