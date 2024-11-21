from shared import All_Books, save_books_to_file

def remove_book():
    isbn_to_remove = int(input("Enter ISBN of the book to remove: "))
    book_found = False

    for book in All_Books:
        if book["isbn"] == isbn_to_remove:
            All_Books.remove(book)
            book_found = True
            save_books_to_file()
            print("\nBook Details:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Publishing Year: {book['pub_year']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            print(f"\t\tBook with ISBN {isbn_to_remove} removed successfully.")
            break

    if not book_found:
        print(f"\t\tNo book found with ISBN {isbn_to_remove}.")