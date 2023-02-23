import sqlite3


# Data layer in MVC - Model View Controller Pattern
# Models is the binding that associates DB tables with associated functions.

# 2. Create a connection to DB
conn = sqlite3.connect('todo.db')

# 3. Write your sql query
query = "<SQLite Query goes here"

# 4. execute the query
result = conn.execute(query)


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table?

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
    
        );
        """
        self.conn.execute(query)

    def create_user_table(self):
        #Create a user table in similar fasihon
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            _id INTEGER PRIMARY KEY,
            Name TEXT,
            CreatedOn Date DEFAULT CURRENT_DATE 

        );
        
        """
        self.conn.execute(query)


class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn
