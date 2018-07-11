from flask import Flask
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/patientdb"
mongo = PyMongo(app)

@app.route('/add')
def add():
    mongo.db.users.insert({'name' : 'james', 'color':'black'})
    return 'Added User!'



if __name__ == '__main__':
    app.run(debug=True)
