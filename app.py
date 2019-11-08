# In utils folder there is DB related stuff
from utils import database as database


def menu():
    database.create_book_file()
    user_input = input("user choice")
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            prompt_read_books()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print("unknown command")

        user_input = input("user choice")


def prompt_add_book():   # Fuction for adding books
    name = input("enter name of the book")
    author = input("enter the author of the book")

    database.add_book(name, author)


def list_books():   # ALl books are shown here
    books = database.get_all_books()   # This get all the books from DB
    for book in books:
        # yes will come if book == true else no
        read = "Yes" if book["read"] else "No"
        # printing books list by fstring
        print(f"Book {book['name']} By Author {book['author']} is read {read}")


def prompt_read_books():   # function to return Yes for read books else No
    name = input("enter name of the book read:")

    database.mark_book_as_read(name)


def prompt_delete_book():   # function to delete books
    name = input("enter the name of the book")

    database.delete_book(name)


menu()
