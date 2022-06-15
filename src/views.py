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


def default_calc_results():
    calc_results = {'txtCaCO3': 0,
                    'txtNaHCO3': 0,
                    'txtCaSO4': 0,
                    'txtCaCl2': 0,
                    'txtMgSO4': 0,
                    'txtNaCl': 0,
                    'residual': 0} 

    return calc_results


ah = aguaHefe.aguaHefe()

'''
@app.route("/")
def home():
    return render_template('home.html', styles=styles_data)
'''


@app.route("/", methods=('GET', 'POST'))
def home():
    form_data = {}

    if request.method == 'GET':
        return render_template('home.html', form_data=form_data, styles=styles_data, calc_results=default_calc_results())

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

        calc_results = {'txtCaCO3': txtCaCO3 * int(form_data['txtmashvolume']),
                        'txtNaHCO3': txtNaHCO3 * int(form_data['txtmashvolume']),
                        'txtCaSO4': txtCaSO4 * int(form_data['txtmashvolume']),
                        'txtCaCl2': txtCaCl2 * int(form_data['txtmashvolume']),
                        'txtMgSO4': txtMgSO4 * int(form_data['txtmashvolume']),
                        'txtNaCl': txtNaCl * int(form_data['txtmashvolume']),
                        'residual': residual}           
        
        return render_template('home.html', form_data=form_data, styles=styles_data, calc_results=calc_results)
 
 
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
