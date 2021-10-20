import json
import mysql.connector


def connect():

    with open("files/dbAccessData.json") as dbFile:
        db_dict = json.load(dbFile)

        try:
            return mysql.connector.connect(
                host=db_dict["host"],
                user=db_dict["user"],
                password=db_dict["password"],
                database=db_dict["database"]
            )

        except mysql.connector.Error:
            print("Can not connect to database")
            return None
