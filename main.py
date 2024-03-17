#import our necessary dependencies
from flask import Flask, request, jsonify
# then import your models and the database:
from db import db
from Author import Author
from Book import Book

app = Flask(__name__)

# and then in the next step, we connect to the database like so:
# [ here, you go to ElephantSQL and copy/paste the string]
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kxgacqnx:qvjaMSQRj8bBAveiOlMkvY-LVHiE659L@cornelius.db.elephantsql.com/kxgacqnx"

# so basically, SQLAlchemy looks through your app's config and specifically
# looks for this variable for the connection string

# we need to hook thie database and the app together like this:
db.init_app(app)

# now create authors:
@app.get("/")
def createAuthors():
  bob = Author(name="Bob")
  alice = Author(name="Alice")
  db.session.add_all([bob,alice])
  # finalize the transaction and add these authors to database
  db.session.commit()
  return "Created authors"
# as the last step (at the end of the file):

@app.post("/author1")
def addToAuthor1():
		# for the first step, we will find the author with id=1
    bob = db.session.execute(db.select(Author).filter_by(id=1)).scalar_one()
    #print(hussain.__dict__)
		#then we need to get the data from the request body
    data = request.get_json()
    bookToAdd = Book(name=data["name"], author=bob)
		# then add the book
    db.session.add(bookToAdd)
    db.session.commit()
		# return the new object
    return {"name" : bookToAdd.name , "id" : bookToAdd.id}

@app.post("/author2")
def addToAuthor2():
    alice = db.session.execute(db.select(Author).filter_by(id=2)).scalar_one()
    data = request.get_json()
    bookToAdd = Book(name=data["name"], author=alice)
    db.session.add(bookToAdd)
    db.session.commit()
    return {"name" : bookToAdd.name , "id" : bookToAdd.id}

@app.get("/author1")
def getAuthor1():
		# get for the first author:
    bookToFind = db.session.execute(db.select(Book).filter_by(author_id=1)).scalars()
    finder =  bookToFind.all() #find all books
    result = []
    for items in finder: #convert response into a dictionary
        result.append({"name" :  items.name, "id" : items.id})

    return jsonify(result) #return
    
@app.get("/author2")
def getAuthor2():
    bookToFind = db.session.execute(db.select(Book).filter_by(author_id=2)).scalars()
    finder =  bookToFind.all()
    result = []
    for items in finder:
        result.append({"name" :  items.name, "id" : items.id})
    return jsonify(result)

if __name__ == "__main__":
    with app.app_context():
				# while the server is running, connect to database and create the tables
        db.create_all()        
		# run the server and enable the debugger
    app.run(debug=True)
