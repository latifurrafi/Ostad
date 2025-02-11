All_books = []

def add_books(All_books):
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")
    isbn = int(input("Enter ISBN Number : "))
    pub_year = int(input("Enter Publishing Year : "))
    price = int(input("Enter Book Price : "))
    quantity = int(input("Enter Quantity Number : "))

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "pub_year" : pub_year,
        "price" : price,
        "quantity" : quantity
    }
    All_books.append(book)
    save_all_books(All_books)
    print("\t\tBooks Added Successully")
    return All_books

def save_all_books(All_books):
    with open("All_Books.csv", "w") as file:
        for book in All_books:
            content = f"{book["title"]} || {book["author"]} || {book["isbn"]} || {book["pub_year"]} || {book["price"]} || {book["quantity"]}\n"
            file.write(content)

def view_all_books(All_Books):
    if All_Books:
        for book in All_Books:
            print(f"Title: {book['title']} || Author: {book['author']} || Isbn_number: {book['isbn']} || Publishing_year: {book['pub_year']} || Price: {book['price']} || Quantity: {book['quantity']}")
    else:
        print("No Book Found In File")

while True:
    print("\n\t\t\tWelcome To Library Management System")
    print("\t\t\t\t1. Add Books")
    print("\t\t\t\t2. View All Books")
    print("\t\t\t\t3. Exit")

    option = input("Select Any Number : ")

    if option == "1":
       All_books = add_books(All_books)
    elif option == "2":
        view_all_books(All_books)
    elif option == "3":
        print("\t\tThanks For Using Library Management System")
        break
    else:
        print("\t\tInvalid Choice")
   