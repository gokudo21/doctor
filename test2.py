from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

@app.route("/register")
def register_view():
    return render_template('register.html')

@app.route('/hope')
def hope():
    mongo.db.patients.insert({'doctor_name': 'james', 'patient_name': 'black'})
    return 'hope worked!'

@app.route('/pdata',methods = ['POST', 'GET'])
def pdata():
    docnamey = request.args.get('docname')
    patnamey = request.args.get('patname')
    civilnamey = request.args.get('civilname')
    agenamey = request.args.get('agename')
    Sexnamey = request.args.get('Sexname')
    roomnamey = request.args.get('roomname')
    Healthnamey = request.args.get('Health')
    statusnamey = request.args.get('status')
    Medicinesnamey = request.args.get('Medicines')
    Elementdnamey = request.args.get('Elementdite')
    recommendationnamey = request.args.get('drecommendation')
    notenamey = request.args.get('pnote')


    patients = mongo.db.patients
    patients.insert({'doctor_name' : docnamey, 'patient_name' : patnamey, 'civil_ID' : civilnamey, 'age' : agenamey, 'sex' : Sexnamey, 'room_number' : roomnamey,'health_history' : Healthnamey, 'patient_status' : statusnamey, 'medicines' : Medicinesnamey, 'element_diet' : Elementdnamey, 'doctor_recommendation': recommendationnamey, 'note': notenamey})

    return 'added ' + patnamey + 'to the database!'


if __name__ == '__main__':
    app.run(debug=True)