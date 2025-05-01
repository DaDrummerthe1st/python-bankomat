import sqlite3
#from sqlitedict import SqliteDict

from easygui import msgbox

class ConnectDatabase:
    def __init__(self):
        self.database = "bank.db"

    def connect(self):
        try:
            connection = sqlite3.connect(self.database)
        except sqlite3.OperationalError as e:
            return e
        else:
            try:
                cursor = connection.cursor()
            except sqlite3.OperationalError as e:
                return e
            else:
                return cursor

db = ConnectDatabase()
db.connect()
db.cursor # why does it not find this?!