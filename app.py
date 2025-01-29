from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
books=[
    {"id":1,"title":"1984","author":"George Orwell"},
    {"id":2,"title":"to kill a mockingbird","author":"Harper Lee"},
    {"id":3,"title":"ΤΑ ΔΑΚΡΥΑ ΤΟΥ ΘΕΟΥ","author":"ΧΡΥΣΗΙΔΑ ΔΗΜΟΥΛΙΔΟΥ"}
]
@app.route("/")
def home():
    return render_template("index.html",books=books)
#restful api routes
@app.route("/api/books",methods=['GET'])
def get_books():
    return jsonify(books)
@app.route("/api/books/<int:book_id>",methods=['GET'])
def get_book(book_id):
    #generator
    book= next((book for book in books if book['id']==book_id),None)
    return jsonify(book) if book else('',404)
@app.route("/api/books",methods=['POST'])
def add_book():
    new_book= request.json
    new_book["id"]=len(new_book)+1
    books.append(new_book)
    return jsonify(new_book),201
@app.route("/api/books/<int:book_id>",methods=['PUT'])
def update_book(book_id):
    book= next((book for book in books if book['id']==book_id),None)
    if book:
        updated_book=request.json
        book.update(updated_book)
    return jsonify(updated_book) if updated_book else ('',404)
#delete
@app.route("/api/books/<int:book_id>",methods=['DELETE'])
def delete_book(book_id):
    global books
    books=[(book for book in books if book['id']!=book_id)]
    return ('',204)
if __name__=='__main__':
    app.run(debug=True)
 
