from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

@app.route("/register")
def register_view():
    return render_template('register.html')

@app.route("/ID")
def ID_view():
    return render_template('ID.html')

@app.route('/hope')
def hope():
    mongo.db.patients.insert({'doctor_name': 'james', 'patient_name': 'black'})
    return 'hope worked!'

@app.route('/pdata/<dname>/<pname>',methods = ['POST', 'GET'])
def pdata(dname, pname):
    docnamey = request.args.get('docname')
    patnamey = request.args.get('patname')

    patients = mongo.db.patients
    patients.insert({'dname' : docnamey, 'pname' : patnamey})

    return 'added ' + patnamey + 'to the database!'

@app.route('/find',methods = ['POST', 'GET'])
def find():
    searchy = request.args.get('search')

    patients = mongo.db.patients
    searchy = patients.find_one({'pname' : searchy})
    return 'found  ' + searchy['pname'] + 'his doc name is ' + searchy['dname']

1

if __name__ == '__main__':
    app.run(debug=True)
