menu = "\n Enter 'a' to add books, 'l' to check list of books, 'f' to find a book, 'q' to quit: "
books = []


def add():
    name_of_book = input("Name of Book: ")
    name_of_author = input("Name of Author: ")
    year_of_book = input("Year of Book: ")
    publisher = input("Name of Publisher: ")

    books.append({
        "book_name": name_of_book,
        "author": name_of_author,
        "year": year_of_book,
        "publisher": publisher
    })


# add()


def show_books():
    for x in books:
        print_books(x)
        '''print(f'BookName: , {l["books"]}\n,'
              f'Author: , {l["books"]}\n,'
              f'Year: , {l["books"]}\n,'
              f'Publisher:, {l["books"]}')'''


# showbooks()

def print_books(x):
    print(f"Book Name: {x['book_name']}")
    print(f"Author: {x['author']}")
    print(f"Year: {x['year']}")
    print(f"Publisher: {x['publisher']}\n")


def find_books():
    name = input("Enter Book name: ".casefold())
    for x in books:
        if x["book_name"] == name:
            print_books(x)


# user = dict(a=add, l=show_books, f=find_books)

user = {
    'a': add,
    'l': show_books,
    'f': find_books,
}


def home():
    selection = input(menu)
    while selection != "q":
        if selection in user:
            selection_function = user[selection]
            selection_function()
        else:
            print("Unknown Command. Please try again")
        selection = input(menu)


home()
