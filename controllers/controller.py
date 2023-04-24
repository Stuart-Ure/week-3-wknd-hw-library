from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book import *

# @app.route('/books')
# def index():
#     return render_template('index.jinja', title = "Library" , book_list = book_list)

@app.route('/books')
def index():
    return render_template('index.jinja', title="Library", books=books)


@app.route("/books/<index>") 
def show_book(index):
    return render_template("book_details.jinja", book=books[int(index)])

@app.route('/books', methods = ['POST'])
def add_book():
    title = request.form ['title']
    author = request.form ['author']
    genre = request.form ['genre']
    new_book= Book(title= title, author = author, genre = genre,)
    add_new_book(new_book)
    return redirect ("/books") 
    

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')
