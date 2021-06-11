
from PyQt5 import QtCore, QtGui, QtWidgets
import threading

from main import mainfirebaseinteraction


mainthread = threading.Thread(target=mainfirebaseinteraction)


class Ui_StartPage(object):

    def openWindow(self):
        from Search import Ui_SearchPage
        print("thread started")
        mainthread.start()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SearchPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 700)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label_bg = QtWidgets.QLabel(Dialog)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label_bg.setStyleSheet("background-image: url(:/newPrefix/BG-FB1.jpg);")
        self.label_bg.setText("")
        self.label_bg.setIndent(-12)
        self.label_bg.setObjectName("label_bg")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 660, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(170, 320, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(9, 13, 84);\n""")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 280, 241, 131))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 13, 84);\n""")
        self.label_2.setObjectName("label_2")
        self.labe_logo = QtWidgets.QLabel(Dialog)
        self.labe_logo.setGeometry(QtCore.QRect(240, 150, 201, 151))
        self.labe_logo.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.labe_logo.setText("")
        self.labe_logo.setObjectName("labe_logo")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(260, 430, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("QPushButton{\n"
"border-radius : 20;\n"
"background-color: rgb(20,135,193);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(16,108,154);\n"
"color:rgb(249,253,254);\n"
"}\n"
"QpushButton:pressed{\n"
"background-color: rgb(rgb(17,116,175));\n"
"}\n"
"")
        self.start.setAutoDefault(True)
        self.start.setDefault(False)
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.openWindow)
        self.start.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Copyright @2021  Build By  Priyansh | Tulika | Umeed"))
        self.label_1.setText(_translate("Dialog", "FACE"))
        self.label_2.setText(_translate("Dialog", "GRAB"))
        self.start.setText(_translate("Dialog", "START"))
import imgs_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_StartPage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

