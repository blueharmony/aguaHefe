import numpy as np
from scipy.optimize import nnls

# https://www.brewersfriend.com/water-chemistry/
# https://andreask.cs.illinois.edu/cs357-s15/public/demos/06-qr-applications/Solving%20Least-Squares%20Problems.html
# https://dwightreid.com/blog/2015/09/21/python-how-to-solve-simultaneous-equations/
# https://math.stackexchange.com/questions/3579710/computer-tools-to-solve-linear-system-of-equations-with-singular-matrix

gallons = 10


def calculateSalts(target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3):
    # the effects on 1 gram of each salt
    A1 = [53,    0,  62,  72,   0,   0]
    A2 = [0,     0,   0,   0,  26,   0]
    A3 = [0,     0, 147,   0, 103,   0]
    A4 = [0,    75,   0,   0,   0, 104]
    A5 = [0,     0,   0, 127,   0, 160]
    A6 = [161, 191,   0,   0,   0,   0]
    A = np.array([A1, A2, A3, A4, A5, A6])

    # setup our targets
    B = np.array([target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3])
    print()
    print("-------------------")    
    print("Targets: Ca, Mg, SO4, Na, Cl, HCO3")
    print("        ", target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)

    # only positive values from a non-linear approximation
    answer_array, residual = nnls(A, B)
    # print("answer array: ", answer_array)
    # print("residual: ", residual)

    # get individual salts from the returned array
    CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl = answer_array

    return CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual


def printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual):

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


if __name__ == "__main__":
    
    # Munich (Dark Lager)
    target_Ca = 82
    target_Mg = 20
    target_SO4 = 16
    target_Na = 4
    target_Cl = 2
    target_HCO3 = 320
    
    CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual = \
        calculateSalts(target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)
    printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual)

    # Light colored and hoppy
    target_Ca = 75
    target_Mg = 5
    target_SO4 = 150
    target_Na = 10
    target_Cl = 50
    target_HCO3 = 0
    
    CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual = \
        calculateSalts(target_Ca, target_Mg, target_SO4, target_Na, target_Cl, target_HCO3)
    printResults(CaCO3, NaHCO3, CaSO4, CaCl2, MgSO4, NaCl, residual)
