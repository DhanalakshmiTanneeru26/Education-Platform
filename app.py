from flask import Flask, render_template
app = Flask(__name__)

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

@app.route('/Signup')
def signup():
    return render_template('signup.html')

@app.route('/Login')
def login():
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