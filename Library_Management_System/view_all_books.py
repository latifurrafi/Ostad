from shared import All_Books

def view_all_books():
    if All_Books:
        for book in All_Books:
            print(f"Title: {book['title']} || Author: {book['author']} || ISBN: {book['isbn']} || Year: {book['pub_year']} || Price: {book['price']}  || Quantity: {book['quantity']}")
    else:
        print("No books found in the library.")