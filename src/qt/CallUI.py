#CallUI.py
import sys
from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os 

class CallUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CallUI, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        # QtWidgets.QWidget.__init__(self)
        # self.w = QtWidgets.QMainWindow()
        self.ui.setupUi(self)
        # self.setUpBtnconnect()

    #def setUpBtnconnect(self):
    #    self.ui.pushButton.clicked.connect(self.myFunction)

    def myFunction(self):
        os.system("ipconfig")
        raw_input()

def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())
