from flask import flask, render_template,  url_for, request, session, redirect
from flask.ext.pymongo import pymongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb://pretty:'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'you are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name'  :  request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db,users
        existing_user = users.find_one({'name'  :  request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.genSalt())
            users.insert({'name'  :  request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'that username already exists!'

    return render_template(register.html)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)


