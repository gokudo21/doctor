
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)


#app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
#app.config['MONGO_URI'] = 'mongodb://gokudo21:a1234567@ds018848.mlab.com:18848/patientdb'


mongo = PyMongo(app)


@app.route("/login")
def serve():
    return render_template('login.html')

@app.route("/ID")
def ID_view():
    return render_template('ID.html')

@app.route("/register")
def register_view():
    return render_template('register.html')

@app.route("/room1")
def room1_view():
    patients = mongo.db.patients
    result = patients.find_one({'room_number': "1"})
    return render_template('room1.html', record=result)

@app.route("/room2")
def room2_view():
    patients = mongo.db.patients
    result = patients.find_one({'room_number': "2"})
    return render_template('room2.html', record=result)


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

    return render_template('ID.html')


@app.route('/patient_info',methods = ['POST', 'GET'])
def find():
    searchy = request.args.get('search')
    patients = mongo.db.patients
    result = patients.find_one({'civil_ID' : searchy})
    print('result: ')
    print(result)

    return render_template('patient_info.html', record=result)




@app.route('/login_data',methods = ['POST', 'GET'])
def login_data():
    passwordy = request.args.get('psw')
    useridy = request.args.get('userid')
    if passwordy == "1234567" and useridy == "haya" or  passwordy == "7654321" and useridy == "manal":
        return render_template('ID.html')
    else :
        return render_template('login.html')

@app.route("/test6")
def serve6():
    return render_template('test6.html')


@app.route('/edit', methods=['GET'])
def edit():
    search2y = request.args.get('search2')
    patients = mongo.db.patients
    result5 = patients.find_one({'civil_ID': search2y})
    print("result 5:")
    print(result5)
    print("search: ")
    print(search2y)
    return render_template('edit.html', record=result5)

@app.route('/edit2',methods = ['POST', 'GET'])
def edit2():
    docname2y = request.args.get('docname2')
    patname2y = request.args.get('patname2')
    civilname2y = request.args.get('civilname2')
    agename2y = request.args.get('agename2')
    Sexname2y = request.args.get('Sexname2')
    roomname2y = request.args.get('roomname2')
    Healthname2y = request.args.get('Health2')
    statusname2y = request.args.get('status2')
    Medicinesname2y = request.args.get('Medicines2')
    Elementdname2y = request.args.get('Elementdite2')
    recommendationname2y = request.args.get('drecommendation2')
    notename2y = request.args.get('pnote2')

    patients = mongo.db.patients
    #1patients.update({'name': 'target'}, {'school': 'new school', 'age': 'new age'})

    patients.update({'civil_ID': civilname2y} ,{ 'doctor_name': docname2y, 'patient_name': patname2y, 'civil_ID': civilname2y, 'age': agename2y, 'sex': Sexname2y,'room_number': roomname2y, 'health_history': Healthname2y, 'patient_status': statusname2y,'medicines': Medicinesname2y, 'element_diet': Elementdname2y, 'doctor_recommendation': recommendationname2y,'note': notename2y})

    return patname2y + ' updated'



if __name__ == '__main__':
    app.run(debug=True)