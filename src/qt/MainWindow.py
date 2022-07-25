# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 200, 621, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 510, 621, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 760, 621, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 10, 621, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"background-color: rgb(219, 255, 196);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 140, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(190, 110, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 255);")
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(250, 30, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 353, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 220, 621, 291))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_7.setGeometry(QtCore.QRect(410, 30, 61, 31))
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_8.setGeometry(QtCore.QRect(480, 30, 61, 31))
        self.textEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_5.setGeometry(QtCore.QRect(270, 30, 61, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 30, 61, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_6.setGeometry(QtCore.QRect(340, 30, 61, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_9.setGeometry(QtCore.QRect(550, 30, 61, 31))
        self.textEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 70, 631, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.targetHCO3 = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetHCO3.setGeometry(QtCore.QRect(550, 20, 61, 41))
        self.targetHCO3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetHCO3.setObjectName("targetHCO3")
        self.targetSO4 = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetSO4.setGeometry(QtCore.QRect(340, 20, 61, 41))
        self.targetSO4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetSO4.setObjectName("targetSO4")
        self.targetCa = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetCa.setGeometry(QtCore.QRect(200, 20, 61, 41))
        self.targetCa.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetCa.setObjectName("targetCa")
        self.targetMg = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetMg.setGeometry(QtCore.QRect(270, 20, 61, 41))
        self.targetMg.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetMg.setObjectName("targetMg")
        self.targetCl = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetCl.setGeometry(QtCore.QRect(480, 20, 61, 41))
        self.targetCl.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetCl.setObjectName("targetCl")
        self.targetNa = QtWidgets.QTextEdit(self.groupBox_6)
        self.targetNa.setGeometry(QtCore.QRect(410, 20, 61, 41))
        self.targetNa.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.targetNa.setObjectName("targetNa")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 140, 621, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_20 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_20.setGeometry(QtCore.QRect(550, 20, 61, 41))
        self.textEdit_20.setStyleSheet("background-color: transparent;")
        self.textEdit_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_20.setReadOnly(True)
        self.textEdit_20.setObjectName("textEdit_20")
        self.textEdit_24 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_24.setGeometry(QtCore.QRect(270, 20, 61, 41))
        self.textEdit_24.setStyleSheet("background-color: transparent;")
        self.textEdit_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_24.setReadOnly(True)
        self.textEdit_24.setObjectName("textEdit_24")
        self.textEdit_21 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_21.setGeometry(QtCore.QRect(480, 20, 61, 41))
        self.textEdit_21.setStyleSheet("background-color: transparent;")
        self.textEdit_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_21.setReadOnly(True)
        self.textEdit_21.setObjectName("textEdit_21")
        self.textEdit_22 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_22.setGeometry(QtCore.QRect(410, 20, 61, 41))
        self.textEdit_22.setStyleSheet("background-color: transparent;")
        self.textEdit_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_22.setReadOnly(True)
        self.textEdit_22.setObjectName("textEdit_22")
        self.textEdit_23 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_23.setGeometry(QtCore.QRect(340, 20, 61, 41))
        self.textEdit_23.setStyleSheet("background-color: transparent;")
        self.textEdit_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_23.setReadOnly(True)
        self.textEdit_23.setObjectName("textEdit_23")
        self.textEdit_19 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_19.setGeometry(QtCore.QRect(200, 20, 61, 41))
        self.textEdit_19.setStyleSheet("background-color: transparent;")
        self.textEdit_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_19.setReadOnly(True)
        self.textEdit_19.setObjectName("textEdit_19")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 210, 621, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_25 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_25.setGeometry(QtCore.QRect(550, 20, 61, 41))
        self.textEdit_25.setStyleSheet("background-color: transparent;")
        self.textEdit_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_25.setReadOnly(True)
        self.textEdit_25.setObjectName("textEdit_25")
        self.textEdit_27 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_27.setGeometry(QtCore.QRect(410, 20, 61, 41))
        self.textEdit_27.setStyleSheet("background-color: transparent;")
        self.textEdit_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_27.setReadOnly(True)
        self.textEdit_27.setObjectName("textEdit_27")
        self.textEdit_30 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_30.setGeometry(QtCore.QRect(200, 20, 61, 41))
        self.textEdit_30.setStyleSheet("background-color: transparent;")
        self.textEdit_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_30.setReadOnly(True)
        self.textEdit_30.setObjectName("textEdit_30")
        self.textEdit_28 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_28.setGeometry(QtCore.QRect(340, 20, 61, 41))
        self.textEdit_28.setStyleSheet("background-color: transparent;")
        self.textEdit_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_28.setReadOnly(True)
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_29.setGeometry(QtCore.QRect(270, 20, 61, 41))
        self.textEdit_29.setStyleSheet("background-color: transparent;")
        self.textEdit_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_29.setReadOnly(True)
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_26 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_26.setGeometry(QtCore.QRect(480, 20, 61, 41))
        self.textEdit_26.setStyleSheet("background-color: transparent;")
        self.textEdit_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_26.setReadOnly(True)
        self.textEdit_26.setObjectName("textEdit_26")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 530, 621, 271))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_43 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_43.setGeometry(QtCore.QRect(30, 230, 241, 31))
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_40 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_40.setGeometry(QtCore.QRect(280, 190, 61, 31))
        self.textEdit_40.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_40.setReadOnly(False)
        self.textEdit_40.setObjectName("textEdit_40")
        self.textEdit_35 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_35.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.textEdit_35.setObjectName("textEdit_35")
        self.textEdit_41 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_41.setGeometry(QtCore.QRect(30, 190, 241, 31))
        self.textEdit_41.setObjectName("textEdit_41")
        self.textEdit_38 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_38.setGeometry(QtCore.QRect(280, 150, 61, 31))
        self.textEdit_38.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_38.setReadOnly(False)
        self.textEdit_38.setObjectName("textEdit_38")
        self.textEdit_33 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_33.setGeometry(QtCore.QRect(280, 30, 61, 31))
        self.textEdit_33.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_33.setReadOnly(False)
        self.textEdit_33.setObjectName("textEdit_33")
        self.textEdit_34 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_34.setGeometry(QtCore.QRect(280, 110, 61, 31))
        self.textEdit_34.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_34.setReadOnly(False)
        self.textEdit_34.setObjectName("textEdit_34")
        self.textEdit_37 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_37.setGeometry(QtCore.QRect(30, 70, 241, 31))
        self.textEdit_37.setObjectName("textEdit_37")
        self.textEdit_32 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_32.setGeometry(QtCore.QRect(30, 30, 241, 31))
        self.textEdit_32.setObjectName("textEdit_32")
        self.textEdit_36 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_36.setGeometry(QtCore.QRect(280, 70, 61, 31))
        self.textEdit_36.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_36.setReadOnly(False)
        self.textEdit_36.setObjectName("textEdit_36")
        self.textEdit_39 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_39.setGeometry(QtCore.QRect(30, 150, 241, 31))
        self.textEdit_39.setObjectName("textEdit_39")
        self.textEdit_42 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_42.setGeometry(QtCore.QRect(280, 230, 61, 31))
        self.textEdit_42.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.textEdit_42.setReadOnly(False)
        self.textEdit_42.setObjectName("textEdit_42")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 26))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Desktop/materials-qt-designer-python/sample_editor/ui/resources/help-content.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionContact = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../Desktop/materials-qt-designer-python/sample_editor/ui/resources/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContact.setIcon(icon1)
        self.actionContact.setObjectName("actionContact")
        self.menuHome.addAction(self.actionAbout)
        self.menuHome.addAction(self.actionContact)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Target Water Data:"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Salts"))
        self.pushButton.setText(_translate("MainWindow", "Update Target Minerals"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Water Volume (total):"))
        self.lineEdit.setText(_translate("MainWindow", "10"))
        self.groupBox.setTitle(_translate("MainWindow", "Units:"))
        self.radioButton.setText(_translate("MainWindow", "Gallons"))
        self.radioButton_2.setText(_translate("MainWindow", "Quarts"))
        self.radioButton_3.setText(_translate("MainWindow", "Liters"))
        self.label.setText(_translate("MainWindow", "Target Profile:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Water Chemistry - Ion Levels (ppm or mg/L):"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Na</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">+</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Cl</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">-</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Mg</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">+2</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Ca</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">+2</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">4</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">-2</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">HCO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">3</span><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">-</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Target:"))
        self.targetHCO3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.targetSO4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.targetCa.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.targetMg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.targetCl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.targetNa.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Adjustments From Salts:"))
        self.textEdit_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Difference:"))
        self.textEdit_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_27.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_30.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_29.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.textEdit_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Optimized Brewing Salts Additions:"))
        self.textEdit_43.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Canning Salt NaCl</span></p></body></html>"))
        self.textEdit_40.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_35.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Gypsom CaSO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">4</span></p></body></html>"))
        self.textEdit_41.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Epsom Salt MgSO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">4</span></p></body></html>"))
        self.textEdit_38.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_33.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_34.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_37.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Baking Soda NaHCO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">3</span></p></body></html>"))
        self.textEdit_32.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Chalk CaCO</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">3</span></p></body></html>"))
        self.textEdit_36.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_39.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Calcium Chloride CaCl</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">2</span></p></body></html>"))
        self.textEdit_42.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout.setToolTip(_translate("MainWindow", "About thie application"))
        self.actionContact.setText(_translate("MainWindow", "Contact..."))
        self.actionContact.setToolTip(_translate("MainWindow", "Whom to contact with questions/suggestions"))

