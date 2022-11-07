from flask import Flask, request, render_template, session
import mysql.connector
import datetime
import json

app = Flask(__name__)
app.secret_key = "very very secret. So secret in fact that it is visible to the entire world on GitHub"

@app.route("/", methods=["GET", "POST"])
def main():
    f = open("../CREDENTIALS.json")
    credentials = json.load(f)
    f.close()

    database = mysql.connector.connect(**credentials["database"]) # create database object
    cursor = database.cursor()

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
        spot_id = request.form.get("spot_id")

        print(name)
        print(student_num)
        print(exam_name)
        print(instructor_contact)
        print(exam_start)
        print(exam_duration)
        print(last_time_checked)
        print(needs_help)
        print(started)

        cursor.execute(f"INSERT INTO exam_info VALUES (\"{name}\", {student_num}, \"{exam_name}\", \"{instructor_contact}\", \"{exam_start}\", {exam_duration}, \"{last_time_checked}\", {int(needs_help)}, {int(started)}, {spot_id})")
        database.commit()
        cursor.close()
        database.close()
        return render_template("next_page.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run()