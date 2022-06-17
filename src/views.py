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
        return render_template('home.html',
                                form_data=form_data,
                                styles=styles_data,
                                calc_results=default_calc_results(),
                                salts={})

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

        # convert to selected volume units
        gallons_to_units = ah.gallons2units(int(form_data['txtmashvolume']), form_data['units'])
       
        calc_results = {'txtCaCO3': txtCaCO3 * gallons_to_units,
                        'txtNaHCO3': txtNaHCO3 * gallons_to_units,
                        'txtCaSO4': txtCaSO4 * gallons_to_units,
                        'txtCaCl2': txtCaCl2 * gallons_to_units,
                        'txtMgSO4': txtMgSO4 * gallons_to_units,
                        'txtNaCl': txtNaCl * gallons_to_units,
                        'residual': residual}           
        
        adjustments_from_salts = \
            ah.adjustments_from_salts(  txtCaCO3,
                                        txtNaHCO3,
                                        txtCaSO4,
                                        txtCaCl2,
                                        txtMgSO4,
                                        txtNaCl)
        print(adjustments_from_salts)
        
        # convert the list into a dictionary
        salts_names = ['saltsCa', 'saltsMg', 'saltsSO4', 'saltsNa', 'saltsCl', 'saltsHCO3',
                       'diffCa', 'diffMg', 'diffSO4', 'diffNa', 'diffCl', 'diffHCO3']
        salts = dict(zip(salts_names, adjustments_from_salts))

        return render_template('home.html',
                                form_data=form_data,    
                                styles=styles_data,
                                calc_results=calc_results,
                                salts=salts)


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
