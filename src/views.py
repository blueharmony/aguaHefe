from posixpath import split
from flask import Flask, render_template, request
# from datetime import datetime
import json
# import os
from . import aguaHefe
from . import app

# app = Flask(__name__)


def load_beer_styles(styles_json: str = "styles.json"):
    """ Load the beer styles into memory

    Args:
        styles_json (str, optional): _description_. Defaults to "styles.json".

    Returns:
        JSON: styles data
    """
    # cwd = os.getcwd()
    
    try:
        with open("./src/data/" + styles_json, "r") as f:
            styles_data = json.load(f)
    except FileNotFoundError:
        try:
            with open("./data/styles.json", "r") as f:
                styles_data = json.load(f)
        except FileNotFoundError:
            print("Error: could not find ./src/data/" + styles_json)

    return styles_data


# load the default beer styles
styles_data = load_beer_styles()

# instatiate the aguaHefe class
ah = aguaHefe.aguaHefe()


def default_calc_results():
    """ Set default calculation results to zeros

    Returns:
        dict: zeroed dict values
    """
    calc_results = {'txtCaCO3': 0,
                    'txtNaHCO3': 0,
                    'txtCaSO4': 0,
                    'txtCaCl2': 0,
                    'txtMgSO4': 0,
                    'txtNaCl': 0,
                    'residual': 0} 

    return calc_results


def roundNumber(theNumber, multiplier):
    """ Round theNumber * multiplier to a float

    Args:
        theNumber: the base number
        multiplier: transformation multiplier

    Returns:
        float: formatted number
    """
    answer = theNumber * multiplier
    return "{:.3f}".format(answer)


@app.route("/", methods=('GET', 'POST'))
def home():
    """ The default home page
    """
    form_data = {}
    salts = {}

    # initialize the home form
    if request.method == 'GET':
        print("aguaHefe: GET enter")
        ah_data = {'form_data': form_data, 'styles': styles_data, 'calc_results': default_calc_results(), 'salts': salts}
        return render_template('home.html', ah_data=ah_data)

    # update with values from the form and calculations
    if request.method == 'POST':
        print("aguaHefe: POST enter")
        form_data = request.form

        # best guess at salts needed for water adjustments
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

        # get the gallons2units conversion multiplier
        gallons_to_units = ah.gallons2units(int(form_data['txtmashvolume']), form_data['units'])

        # convert salts amounts to selected volume units       
        calc_results = {'txtCaCO3': roundNumber(txtCaCO3, gallons_to_units),
                        'txtNaHCO3': roundNumber(txtNaHCO3, gallons_to_units),
                        'txtCaSO4': roundNumber(txtCaSO4, gallons_to_units),
                        'txtCaCl2': roundNumber(txtCaCl2, gallons_to_units),
                        'txtMgSO4': roundNumber(txtMgSO4, gallons_to_units),
                        'txtNaCl': roundNumber(txtNaCl, gallons_to_units),
                        'residual': roundNumber(residual, gallons_to_units)}           
        
        # determine how the calculated results will affect the
        # water after adjustments from the salts.
        # also, append the difference between target and calculated
        salts = \
            adjustments_from_salts( txtCaCO3,
                                    txtNaHCO3,
                                    txtCaSO4,
                                    txtCaCl2,
                                    txtMgSO4,
                                    txtNaCl)
        print(salts)

        ah_data = {'form_data': form_data, 'styles': styles_data, 'calc_results': calc_results, 'salts': salts}

        return render_template('home.html', ah_data=ah_data)


@app.route("/bf/")
def bf():
    """ A modified version of the original Brewers Friend page
    """
    return render_template("water-chemistry.html")


@app.route('/calc_salts')
def calc_salts():
    """ background process happening without any refreshing

    Returns:
        _type_: _description_
    """
    args = request.args.get('salts')
    targetCa, targetMg, targetSO4, targetNa, targetCl, targetHCO3, txtMashVolume, txtUnits = args.split(',')

    # best guess at salts needed for water adjustments
    txtCaCO3, txtNaHCO3, txtCaSO4, txtCaCl2, txtMgSO4, txtNaCl, residual = \
        ah.calculateSalts(targetCa, targetMg, targetSO4, targetNa, targetCl, targetHCO3)

    # get the gallons2units conversion multiplier
    gallons_to_units = ah.gallons2units(int(txtMashVolume), txtUnits)

    salts_list = [  roundNumber(txtCaCO3, gallons_to_units), 
                    roundNumber(txtNaHCO3, gallons_to_units), 
                    roundNumber(txtCaSO4, gallons_to_units), 
                    roundNumber(txtCaCl2, gallons_to_units), 
                    roundNumber(txtMgSO4, gallons_to_units), 
                    roundNumber(txtNaCl, gallons_to_units),
                    roundNumber(residual, gallons_to_units)]
    return (json.dumps(salts_list))


def adjustments_from_salts( txtCaCO3,
                            txtNaHCO3,
                            txtCaSO4,
                            txtCaCl2,
                            txtMgSO4,
                            txtNaCl):
    """ Calculate how the salts affect the water

    Args:
        txtCaCO3 (_type_): _description_
        txtNaHCO3 (_type_): _description_
        txtCaSO4 (_type_): _description_
        txtCaCl2 (_type_): _description_
        txtMgSO4 (_type_): _description_
        txtNaCl (_type_): _description_

    Returns:
        salts: dict of salts by salt name
    """

    adjustments_from_salts = \
    ah.adjustments_from_salts(  txtCaCO3,
                                txtNaHCO3,
                                txtCaSO4,
                                txtCaCl2,
                                txtMgSO4,
                                txtNaCl)

    print(adjustments_from_salts)
        
    # convert the list into a dictionary
    # the first six are the salts, the second six are the differences
    salts_names = ['saltsCa', 'saltsMg', 'saltsSO4', 'saltsNa', 'saltsCl', 'saltsHCO3',
                    'diffCa', 'diffMg', 'diffSO4', 'diffNa', 'diffCl', 'diffHCO3']
    salts = dict(zip(salts_names, adjustments_from_salts))

    return salts


@app.route('/adjustments_from_salts')
def adjustments():
    """ Same as above, but returns a JSON string
    """
    args = request.args.get('salts')
    txtCaCO3, txtNaHCO3, txtCaSO4, txtCaCl2, txtMgSO4, txtNaCl = args.split(',')

    salts = \
        ah.adjustments_from_salts(  txtCaCO3,
                                    txtNaHCO3,
                                    txtCaSO4,
                                    txtCaCl2,
                                    txtMgSO4,
                                    txtNaCl)
    return json.dumps(salts)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
