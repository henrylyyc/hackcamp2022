from flask import Flask, request, render_template
import mysql.connector
import json

app = Flask(__name__)

@app.route("/<spot_id>", methods=["GET", "POST"])
def main(spot_id):
    """    f = open("../CREDENTIALS.json")
        credentials = json.load(f)
        f.close()

        database = mysql.connector.connect(**credentials["database"]) # create database object
        cursor = database.cursor()"""
    print(spot_id)
    if request.method == "POST": # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        print(first_name)
        print(last_name)
    return render_template("index.html")

@app.route('/do_thing')
def background_process_test(): # https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event
    print ("Hello")
    return ("nothing")

"""cursor.close()
database.close()"""

if __name__ == "__main__":
    app.run()