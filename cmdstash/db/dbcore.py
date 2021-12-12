import sqlite3


TABLE_TAGS = """CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tags TEXT NOT NULL
    )"""

TABLE_COMMANDS = """CREATE TABLE IF NOT EXISTS commands (
    id INT PRIMARY KEY,
    command TEXT NOT NULL
    )"""


class CommandStashDB:
    def __init__(self, table_name) -> None:
        self.db_name = "cmdstash.db"
        self.table_name = table_name
        self.conn = None
        self._create_tables()

    def _create_tables(self) -> None:
        self._execute_query(TABLE_COMMANDS)
        self._execute_query(TABLE_TAGS)

    def add_records(self, tag) -> None:
        for t in tag:
            query = "INSERT INTO {} ({}) VALUES ('{}')".format(
                self.table_name, 'tags', t
            )
            self._execute_query(query)

    def list_records(self) -> None:
        query = "SELECT * from {}".format(self.table_name)
        res = self._execute_query(query)
        print(res)

    def _execute_query(self, query):
        record = []
        try:
            sqliteConn = sqlite3.connect(self.db_name)
            cursor = sqliteConn.cursor()
            cursor.execute(query)
            if query.startswith("SELECT"):
                record = cursor.fetchall()
            else:
                sqliteConn.commit()
            cursor.close()
        except sqlite3.Error as err:
            print(err)
        finally:
            if sqliteConn:
                sqliteConn.close()
        if record:
            return record
