from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Hackathon'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Services')
def services():
    return render_template('services.html')

@app.route('/Course')
def course():
    return render_template('course.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get user details from the form
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Connect to MongoDB and insert the user details into a 'users' collection
        try:
            users_collection = mongo.db.users
            users_collection.insert_one({'name': name, 'email': email, 'password': hashed_password})
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('signup.html', error=f"Error: {e}")

    return render_template('signup.html')

@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user details from the form
        email = request.form['email']
        password_candidate = request.form['password']

        # Connect to MongoDB and query the user by email
        users_collection = mongo.db.users
        user = users_collection.find_one({'email': email})

        if user:
            # Check the password using Flask-Bcrypt
            if bcrypt.check_password_hash(user['password'], password_candidate):
                # Successful login, redirect to a dashboard or home page
                return redirect(url_for('index'))

        # Incorrect login details, show an error message
        return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

@app.route('/Python')
def python():
    return render_template('python.html')

@app.route('/Html')
def html():
    return render_template('html.html')

@app.route('/Java')
def java():
    return render_template('java.html')

@app.route('/C')
def c():
    return render_template('c.html')

if __name__ == '__main__':
    app.run(debug=True)
