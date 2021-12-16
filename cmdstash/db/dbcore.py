import sqlite3


TABLE_TAGS = """CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name STRING NOT NULL
    )"""

TABLE_COMMANDS = """CREATE TABLE IF NOT EXISTS commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY (tag_id) REFERENCES tags(id)
    )"""

ENABLE_FOREIGN_KEY = """PRAGMA foreign_keys=ON"""


class CommandStashDB:
    def __init__(self, table_name) -> None:
        self.db_name = "cmdstash.db"
        self._create_tables()

    def _create_tables(self) -> None:
        self._execute_query(ENABLE_FOREIGN_KEY)
        self._execute_query(TABLE_COMMANDS)
        self._execute_query(TABLE_TAGS)

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
            exit(1)
        finally:
            if sqliteConn:
                sqliteConn.close()
        if record:
            return record
