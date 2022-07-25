#CallUI.py
import sys
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

# since aguaHefe.py is two folders above, gotta find it
import sys
import pathlib
src_folder = r'{}'.format(pathlib.Path(pathlib.Path(__file__).parent.absolute().parent))
sys.path.append(src_folder)
import aguaHefe

class CallUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # instantiate the ui
        super(CallUI, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # instatiate the aguaHefe class
        self.ah = aguaHefe.aguaHefe()
        ###
        # setup the ui objects
        ###
        # Target Profiles comboBox
        self.styles_data = []
        self.setupTargetProfiles()
        # "Update Target Minerals" button
        self.setUpTargetMineralsButton()

    def setupTargetProfiles(self):
        # load the default beer styles
        self.styles_data = self.ah.load_beer_styles()
        for style in self.styles_data:
            self.ui.comboBox.addItem(style['Style'])
        
    def setUpTargetMineralsButton(self):
        self.ui.pushButton.clicked.connect(self.displayTargetMinerals)

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

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())
