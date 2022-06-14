from flask import Flask, render_template, request
from datetime import datetime
import json
import os
from . import aguaHefe
from . import app

# app = Flask(__name__)

# load the beer styles into memory
# cwd = os.getcwd()
styles_data = ""
try:
    with open("./src/data/styles.json", "r") as f:
        styles_data = json.load(f)
except FileNotFoundError:
    try:
        with open("./data/styles.json", "r") as f:
            styles_data = json.load(f)
    except FileNotFoundError:
        print("Error: could not find .../data/styles.json!")

ah = aguaHefe.aguaHefe()

'''
@app.route("/")
def home():
    return render_template('home.html', styles=styles_data)
'''


@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'GET':
        return render_template('home.html', styles=styles_data)
    if request.method == 'POST':
        form_data = request.form

        txtCaCO3, \
            txtNaHCO3, \
            txtCaSO4, \
            txtCaCl2, \
            txtMgSO4, \
            txtNaCl, \
            residual = \
            ah.calculateSalts(  form_data['targetCa'],
                                form_data['targetMg'],
                                form_data['targetSO4'],
                                form_data['targetNa'],
                                form_data['targetCl'],
                                form_data['targetHCO3'])
        
        return render_template('home.html', form_data=form_data, styles=styles_data)
 
 
@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


'''
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
'''
