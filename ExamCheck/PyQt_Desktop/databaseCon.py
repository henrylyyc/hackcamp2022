import mysql.connector
import json


class DatabaseCon():
    def __init__(self) -> None:
        self.creds = json.load(open("CREDENTIALS.json"))
        self.db = mysql.connector.connect(**self.creds["database"])

    def getUserInfo(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM exam_info")
        self.userInfo = cursor.fetchall()
        return self.userInfo



