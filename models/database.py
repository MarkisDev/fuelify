import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('fuelify.db')

    def execute(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor
