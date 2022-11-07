import serial

from databaseCon import *
from datetime import datetime, timedelta
from PyQt6 import QtCore, QtGui, QtWidgets, QtOpenGLWidgets
from PyQt6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 561)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 33, 69);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(245, 245, 245)")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(245, 245, 245);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet("background-color: rgb(151, 212, 233);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.listWidget.setLineWidth(2)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(99, 196, 232);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleButton)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UBC CFA Arduino Countdown Interfacer"))
        self.label_3.setText(_translate("MainWindow", "UBC Centre for Accesibility"))
        self.label_4.setText(_translate("MainWindow", "Arduino Countdown Interfacer"))
        self.pushButton.setText(_translate("MainWindow", "Upload to Arduino"))

    def addData(self):
        database = DatabaseCon()
        info = database.getUserInfo()

        for entry in info:

            stringToAdd = (
                entry[0] + ", " + str(entry[1]) + ", "
                + entry[2] + ", " + str(entry[4]) + ", "
                + str(entry[5]) + " hours, "
            )

            if entry[8]:
                stringToAdd += "Started"
            else:
                stringToAdd += "Not Started"

            QListWidgetItem(stringToAdd, self.listWidget) 

    def handleButton(self):
        selectedItem = self.listWidget.selectedItems()[0].text().split(", ")
        infoToSend = selectedItem[1] + " " + selectedItem[2]
        
        startTime = datetime.strptime(selectedItem[3], "%Y-%m-%d %H:%M:%S")
        examLengthInMin = float(selectedItem[4][0:3]) * 60
        endTime = startTime + timedelta(minutes = int(examLengthInMin))

        startTimeFormatted = startTime.strftime("%H%M")
        endTimeFormatted = endTime.strftime("%H%M")

        infoToSend += startTimeFormatted + endTimeFormatted

        serDevice = serial.Serial()
        serDevice.port = 'COM5'
        serDevice.baudrate = 115200
        serDevice.timeout = 0.1
        serDevice.open()
        serDevice.write(infoToSend)



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addData()
    MainWindow.show()
    sys.exit(app.exec())
