from models.book import *

book1= Book ("Life of a Rescue Dog", "Kepler Dog", "Autobiography")
book2 = Book (" Edinburgh Beer Guide" ,"Stuart Ure", "Nonfiction")
book3 = Book ("Brewer Dog", "Dave Grohl", " Fiction")
book4 = Book ("Dont Drink and Pyhton", "Mr Coder", "Nonfiction")

books= [book1, book2, book3, book4]

def add_new_book(book):
    books.append(book)

def show_books():
    print(books)
    return books


def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)