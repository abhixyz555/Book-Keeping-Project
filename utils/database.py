import sqlite3   # MYSQL for huge application but sqlLite for small, lightweight & single user applications


def create_book_file():
    # for making connection with the DB
    connection = sqlite3.connect("data.db")
    # now with the help of this cursor we can execute the query
    my_cursor = connection.cursor()
    # Query of MySQL
    create_table_query = "CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)"
    # this function is to execute the query
    my_cursor.execute(create_table_query)
    connection.commit()   # to save all the work in DB
    connection.close()   # to close the function


def add_book(name, author):

    connection = sqlite3.connect("data.db")
    my_cursor = connection.cursor()

    # this method of f-string is not a good practice as it can result in sql injection attacks.
    # insert_query = f"INSERT INTO books VALUES(\"{name}\", \"{author}\", 0)" f-string method

    my_cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("data.db")
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]}
             for row in my_cursor.fetchall()]   # .fetchall is fetching all thr data from table
    # all rows. it will give a list of tuples so we converting it to a dictionary. since
    # we are dictionary in our program

    # connection.commit() No need here because nothing is written to db
    connection.close()
    return books   # last statement as return statement


def mark_book_as_read(name):
    connection = sqlite3.connect("data.db")
    my_cursor = connection.cursor()
    # all data is coming in form of tuple
    my_cursor.execute("UPDATE books SET read = 1 WHERE name = ?", (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect("data.db")
    my_cursor = connection.cursor()
    my_cursor.execute("DELETE FROM books WHERE name = ?", (name,))
    connection.commit()
    connection.close()
