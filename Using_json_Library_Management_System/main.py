import add_books
import view_all_books
import restore_books_file
from datetime import datetime
import update_book_file, delete_book_file

all_books = []

while True:
    print("\n===============================")
    print("       Library Management System")
    print("===============================")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book Information")
    print("4. Remove/Delete a Book")
    print("5. Exit")
    print("===============================")

    all_books = restore_books_file.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        print("Thanks for using Library Management System ")
        break
    else:
        print("Choose a valid number")