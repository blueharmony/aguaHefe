from flask import Flask, render_template, request
from datetime import datetime
from . import app

# app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/data", methods=('GET', 'POST'))
def data():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)
 
 
@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


'''
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
'''
