from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

@app.route("/ID")
def ID_view():
    return render_template('ID.html')



@app.route('/patient_info',methods = ['POST', 'GET'])
def find():
    searchy = request.args.get('search')
    patients = mongo.db.patients
    result = patients.find_one({'civil_ID' : searchy})
    print('result: ')
    print(result)
    return render_template('patient_info.html', record=result)








if __name__ == '__main__':
    app.run(debug=True)
