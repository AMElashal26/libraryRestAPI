#libraryRESTAPI.py

from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask (__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

'''books_list = [
    {
         'id':0,
         "author":"chinua achebe",
         "language":"english",
         "title":"things fall apart",
     },
     {
         'id': 1,
         "author": "hans christian andersen",
         "language": "danish",
         "title": "fairy tales",
     },
     {
         'id': 2,
         "author": "samuel beckett",
         "language": "french,english",
         "title": "molloy,malone dies,the unnamable,the triology",
     },
     {
         'id': 6,
         "author": "jorge luis borges",
         "language": "spanish",
         "title": "ficciones",
     },
     {
         'id': 3,
         "author": "giovanni boccaccio",
         "language": "italian",
         "title": "the decameron",
     },
     {
         'id': 5,
         "author": "emily bront",
         "language": "english",
         "title": "wuthering heights",
     },
]'''

@app.route("/books", methods=['GET','POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()     
        ]
        if books is not None:
            return jsonify(books)
        """
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404"""
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang= request.form['language']
        new_title= request.form['title']
        #id = books_list[-1]['id']+1
        sql = """INSERT INTO book (author, language, title)
                 VALUES (?, ?, ?)"""
        cursor = conn.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201
    
        """new_obj = {
            'id': id,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        books_list.append(new_obj)
        return jsonify(), 201"""

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404
        '''for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass'''
    if request.method == 'PUT':
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """
        
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
                    "id": id,
                    "author": author,
                    "language": language,
                    "title": title
                }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)
        '''for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }
                conn.execute(sql, (author, language, title, id))
                conn.commit()
                return jsonify(updated_book)'''
        

    if request.method == 'DELETE':
        sql=""" DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200

        '''for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)'''

if __name__ == '__main__':
    app.run(debug=True)
