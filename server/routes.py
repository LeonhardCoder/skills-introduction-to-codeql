
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        like_pattern = f"%{name}%"
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE %s", (like_pattern,)
        )
        books = [Book(*row) for row in cursor]

    elif author:
        like_pattern = f"%{author}%"
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE %s", (like_pattern,)
        )
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]
        
    return render_template('books.html', books=books)
