#CallUI.py
import sys
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

# since aguaHefe.py is two folders above, gotta find it
import sys
import pathlib
src_folder = r'{}'.format(pathlib.Path(pathlib.Path(__file__).parent.absolute().parent))
sys.path.append(src_folder)
import aguaHefe as ah

class CallUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # instantiate the ui
        super(CallUI, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # instatiate the aguaHefe class
        self.ah = ah.aguaHefe()
        ###
        # setup the ui objects
        ###

        # Target Profiles comboBox
        self.styles_data = []
        self.setupTargetProfiles()

        # "Update Target Minerals" button
        self.setUpTargetMineralsButton()

        # "Calculate Saltsw" button
        self.setUpCalculateSaltsButton()

        # Units radio buttons
        self.setUpUnitsButtons()

    def setupTargetProfiles(self):
        # load the default beer styles
        self.styles_data = self.ah.load_beer_styles()
        for style in self.styles_data:
            self.ui.comboBox.addItem(style['Style'])
        
    def setUpTargetMineralsButton(self):
        self.ui.updateTargetMineralsButton.clicked.connect(self.displayTargetMinerals)

    def setUpCalculateSaltsButton(self):
        self.ui.calculateSaltsButton.clicked.connect(self.calc_salts)

    def setUpUnitsButtons(self):
        self.ui.radioButton.clicked.connect(self.onClickedUnits)
        self.ui.radioButton_2.clicked.connect(self.onClickedUnits)
        self.ui.radioButton_3.clicked.connect(self.onClickedUnits)

    def getUnits(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            return radioBtn.text()
        else:
            return "Gallons"
            
    def onClickedUnits(self):
        units = self.getUnits()
        print(units)

    def displayTargetMinerals(self):
        combo_index = self.ui.comboBox.currentIndex()
        style = self.styles_data[combo_index]
        print(style)
        self.ui.targetCa.setText(str(style['Ca']))
        self.ui.targetMg.setText(str(style['Mg']))
        self.ui.targetSO4.setText(str(style['SO4']))
        self.ui.targetNa.setText(str(style['Na']))
        self.ui.targetCl.setText(str(style['Cl']))
        self.ui.targetHCO3.setText(str(style['HCO3']))

    def calc_salts(self):
        targetCa = self.ui.targetCa.toPlainText()
        targetMg = self.ui.targetMg.toPlainText()
        targetSO4 = self.ui.targetSO4.toPlainText()
        targetNa = self.ui.targetNa.toPlainText()
        targetCl = self.ui.targetCl.toPlainText()
        targetHCO3 = self.ui.targetHCO3.toPlainText()
        # textMashVolume = self.ui.textMashVolume.text()
        # textUnits = self.getUnits()

        salts = self.ah.calculateSalts(targetCa, targetMg, targetSO4, targetNa, targetCl, targetHCO3)
        print(salts)
        self.ui.txtCaCO3.setText(str(round(salts[0], 3)))
        self.ui.txtNaHCO3.setText(str(round(salts[2], 3)))
        self.ui.txtCaSO4.setText(str(round(salts[3], 3)))
        self.ui.txtCaCl2.setText(str(round(salts[4], 3)))
        self.ui.txtMgSO4.setText(str(round(salts[5], 3)))
        self.ui.txtNaCl.setText(str(round(salts[6], 3)))


def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())
