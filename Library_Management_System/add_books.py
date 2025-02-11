from shared import All_Books, save_books_to_file

def add_books():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter ISBN Number: "))

    for book in All_Books:
        if book["isbn"] == isbn:
            raise ValueError(f"Book with ISBN {isbn} already exists.")

    pub_year = int(input("Enter Publishing Year: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity: "))

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "pub_year": pub_year,
        "price": price,
        "quantity": quantity,
    }
    All_Books.append(new_book)
    save_books_to_file()
    print("\t\tBook added successfully.")
