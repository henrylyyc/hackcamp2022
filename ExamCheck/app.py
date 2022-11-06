from flask import Flask, render_template
import mysql.connector
import json

app = Flask(__name__)

print("yeet")

@app.route("/")
def main():
    """    f = open("../CREDENTIALS.json")
        credentials = json.load(f)
        f.close()

        database = mysql.connector.connect(**credentials["database"]) # create database object
        cursor = database.cursor()"""
    return render_template("index.html")

@app.route('/do_thing')
def background_process_test():
    print ("Hello")
    return ("nothing")

"""cursor.close()
database.close()"""

print("yeet2")

# https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event