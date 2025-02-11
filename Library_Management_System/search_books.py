from shared import All_Books

def search_books():
    isbn_to_search = int(input("Enter ISBN of the book to search: "))
    book_found = False

    for book in All_Books:
        if book["isbn"] == isbn_to_search:
            book_found = True
            print("\nBook Details:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Publishing Year: {book['pub_year']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            break

    if not book_found:
        print(f"\t\tNo book found with ISBN {isbn_to_search}.")