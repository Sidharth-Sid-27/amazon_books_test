from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/authentication')
@auth.login_required
def get_response():
	return jsonify('You are authorized to see this message')
@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'user' and password == 'mylist':
        	return True
        else:
        	return False
    return False

books = [
    {
        "Name": "Time Will Tell",
        "Author": ["Jeffrey Archer"],
        "Genres": ["Saga", "Historical Fiction", "Domestic Fiction"],
        "URL": "https://www.amazon.in/Only-Time-Will-Tell-Chronicles/dp/0330535676"
    },
    {
       "Name": "The Immortals Of Meluha",
       "Author": ["Amish Tripathi"],
       "Genres": ["Novel", "Fantasy Fiction"],
       "URL": "https://www.amazon.in/Immortals-Meluha-Shiva-Trilogy/dp/9380658745"
    }
]

@app.route('/books')
def hello():
    return jsonify(books)

@app.route('/books/add', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return {'id': len(books)}, 200

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    book = request.get_json()
    books[index] = book
    return jsonify(books[index]), 200

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    books.pop(index)
    return 'None', 200