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

    cursor.execute(f"SELECT * FROM exam_info")

    dataDict={}
    #dataTest={}
    for result in cursor:
        #print(result)
        #dataTest[result[9]]=result
        dataDict[result[9]]={"studentName":result[0],
                            "studentNum": result[1],
                            "examName":result[2],
                            "phoneNum":result[3],
                            "examStart":result[4],
                            "duration":result[5],
                            "examEnd":result[6],
                            "needsHelp": result[7],
                            "started": result[8],
                            "isFinished":isFinished(result[4],result[6])
                            }
    
    #print(dataDict)
    if request.method != "POST":
        return render_template("dashboard.html",dataDict=dataDict)


def isFinished(start,end):
    if start >= end:
        return "Done"
    else:
        return "In Progress"

"""cursor.close()
database.close()"""

if __name__ == "__main__":
    app.run()