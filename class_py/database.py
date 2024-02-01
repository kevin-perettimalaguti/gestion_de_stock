import mysql.connector

class Database:
    def __init__(self):
        self.base = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1478",
        database = "store"
        )
        self.request = self.base.cursor()
    
    def closing_connection(self):
        self.base.close()