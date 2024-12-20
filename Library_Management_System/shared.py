import os

All_Books = []

def load_books_from_file():
    if os.path.exists("All_Books.csv"):
        with open("All_Books.csv", "r") as file:
            for line in file:
                if "Title" in line and "Author" in line:
                    continue
                title, author, isbn, pub_year, price, quantity = line.strip().split(" || ")
                title = title.title()
                author = author.title()
                book = {
                    "title": title,
                    "author": author,
                    "isbn": int(isbn),
                    "pub_year": int(pub_year),
                    "price": int(price),
                    "quantity": int(quantity),
                }
                All_Books.append(book)

def save_books_to_file():
    with open("All_Books.csv", "w") as file:
        file.write("Title || Author || ISBN || Year || Price || Quantity\n")
        for book in All_Books:
            book['title'] = book['title'].title()
            book['author'] = book['author'].title()
            content = f"{book['title']} || {book['author']} || {book['isbn']} || {book['pub_year']} || {book['price']} || {book['quantity']}\n"
            file.write(content)


