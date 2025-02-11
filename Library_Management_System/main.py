from shared import load_books_from_file
from add_books import add_books
from view_all_books import view_all_books
from remove_books import remove_book
from search_books import search_books

def main():
    load_books_from_file()

    while True:
        print("\n\t\tWelcome to Library Management System")
        print("\t\t\t1. Add Books")
        print("\t\t\t2. View All Books")
        print("\t\t\t3. Remove Book")
        print("\t\t\t4. Search Book by ISBN")
        print("\t\t\t5. Exit")

        option = input("Select an option: ")
        if option == "1":
            try:
                add_books()
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "2":
            view_all_books()
        elif option == "3":
            remove_book()
        elif option == "4":
            search_books()
        elif option == "5":
            print("\t\tThanks for using the Library Management System.")
            break
        else:
            print("\t\tInvalid choice. Please try again.")

if __name__ == "__main__":
    main()