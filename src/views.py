from posixpath import split
from flask import Flask, render_template, request
# from datetime import datetime
import json
# import os
from . import aguaHefe
from . import app

# app = Flask(__name__)

# instatiate the aguaHefe class
ah = aguaHefe.aguaHefe()

# load the default beer styles
styles_data = ah.load_beer_styles()

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


@app.route("/", methods=(["GET"]))
def home():
    """ The default home page
    """
    salts = {}

    # initialize the home form
    if request.method == 'GET':
        print("aguaHefe: GET enter")
        ah_data = {'styles': styles_data}
        return render_template('home.html', ah_data=ah_data)

""" No longer allow POST requests
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
 """


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


@app.route('/gallons2units')
def gallons2units():
    """ 
    """
    mashvolume = request.args.get('mashvolume')
    units = request.args.get('units')

    multiplier = ah.gallons2units(mashvolume, units)

    return json.dumps(multiplier)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
