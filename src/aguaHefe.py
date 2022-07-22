import numpy as np
from scipy.optimize import nnls
import json

# https://www.brewersfriend.com/water-chemistry/
# https://andreask.cs.illinois.edu/cs357-s15/public/demos/06-qr-applications/Solving%20Least-Squares%20Problems.html
# https://dwightreid.com/blog/2015/09/21/python-how-to-solve-simultaneous-equations/
# https://math.stackexchange.com/questions/3579710/computer-tools-to-solve-linear-system-of-equations-with-singular-matrix

gallons = 10


class aguaHefe:

    # the effects on 1 gram of each salt
    A1 = [53,    0,  62,  72,   0,   0]
    A2 = [0,     0,   0,   0,  26,   0]
    A3 = [0,     0, 147,   0, 103,   0]
    A4 = [0,    75,   0,   0,   0, 104]
    A5 = [0,     0,   0, 127,   0, 160]
    A6 = [161, 191,   0,   0,   0,   0]

    def __init__(self):
        self.A = np.array([self.A1, self.A2, self.A3, self.A4, self.A5, self.A6])
        self.B = np.array([])

    def printResults(self, CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual):
        print("Grams per {:} gallon(s)".format(gallons))
        print()
        print("Chalk CaC03:             {:0.3}".format(CaCO3 * gallons))
        print("Baking Soda NaHCO3:      {:0.3}".format(NaHCO3 * gallons))
        print("Gypsum CaSO4:            {:0.3}".format(CaSO4 * gallons))
        print("Calcium Chloride CaCl2:  {:0.3}".format(CaCl2 * gallons))
        print("Epsom Salt MgSO4:        {:0.3}".format(MgSO4 * gallons))
        print("Canning Salt NaCl:       {:0.3}".format(NaCl * gallons))
        print()
        print("residual: ", residual)

    def load_beer_styles(self, styles_json: str = "styles.json"):
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

    def calculateSalts(self, target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3):
        """_summary_

        Args:
            target_Ca (_type_): _description_
            target_Mg (_type_): _description_
            target_SO4 (_type_): _description_
            target_Na (_type_): _description_
            target_Cl (_type_): _description_
            target_HCO3 (_type_): _description_

        Returns:
            _type_: _description_
        """
        # setup our targets, ensure they are integers

        self.B = np.array([int(target_Ca), int(target_Mg), int(target_SO4), int(target_Na), int(target_Cl), int(target_HCO3)])
        print()
        print("-------------------")    
        print("Targets: Ca, Mg, SO4, Na, Cl, HCO3")
        print("        ", target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)

        # only positive values from a non-linear approximation
        answer_array, residual = nnls(self.A, self.B)
        # get individual salts from the returned array
        CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl = answer_array
        self.printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual)

        return CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual

    def adjustments_from_salts(self, CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl):
        """_summary_

        Args:
            CaCO3 (_type_): _description_
            NaHCO3 (_type_): _description_
            CaSO4 (_type_): _description_
            CaCl2 (_type_): _description_
            MgSO4 (_type_): _description_
            NaCl (_type_): _description_

        Returns:
            _type_: _description_
        """
        salts_amounts = [float(CaCO3), float(NaHCO3), float(CaSO4), float(CaCl2), float(MgSO4), float(NaCl)]

        # transpose the A matrix to treat rows as columns,
        # it's easier to iterate over items in rows
        AT = np.transpose(self.A)

        # create a copy of the transposed matrix,
        # with the salts adjustments applied
        AT_updated = []
        for this_salt, this_array in zip(salts_amounts, AT):
            updated_array = []
            for this_value in this_array:
                updated_array.append(this_salt * this_value)
            AT_updated.append(updated_array)   

        # transpose the updated matrix back to it's original order,
        # because it's easier to add up a row (array) than a column
        A_updated = np.transpose(AT_updated)

        # total up each row (each salt), appending it to a totals list
        totals = []
        for this_array in A_updated:
            total = 0
            for this_value in this_array:
                total += float(this_value)
            totals.append(round(total))

        # calculate diff values between target and actual
        for actual_value, target_value in zip(totals, self.B):
            # append to the same totals
            totals.append(int(actual_value - target_value))

        return totals

    def gallons2units(self, mashvolume, units):
        """_summary_

        Args:
            mashvolume (_type_): _description_
            units (_type_): _description_

        Returns:
            _type_: _description_
        """
        # volume unit conversions, per gallon
        to_gallons = 1
        to_quarts = to_gallons / 4
        to_liters = to_gallons / 3.785

        gallons_to_units = to_gallons  # default
        if (units == 'quarts'):
            gallons_to_units = to_quarts
        if (units == 'liters'):
            gallons_to_units = to_liters

        return int(mashvolume) * gallons_to_units


if __name__ == "__main__":
    ah = aguaHefe()

    # Munich (Dark Lager)
    target_Ca = 82
    target_Mg = 20
    target_SO4 = 16
    target_Na = 4
    target_Cl = 2
    target_HCO3 = 320
    
    CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual = \
        ah.calculateSalts(target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)
    ah.printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual)

    # Light colored and hoppy
    target_Ca = 75
    target_Mg = 5
    target_SO4 = 150
    target_Na = 10
    target_Cl = 50
    target_HCO3 = 0
    
    CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual = \
        ah.calculateSalts(target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)
    ah.printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual)
