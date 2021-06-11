from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import pyrebase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from Start import mainthread

firebaseConfig = {
    "apiKey": " ",
    "storageURL": " ",
    "databaseURL": " ",
    "authDomain": " ",
    "projectId": " ",
    "storageBucket": " ",
    "messagingSenderId": " ",
    "appId": " ",
    "measurementId": " ",
    "serviceAccount": " "
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()
class Ui_SearchPage(object):

    def openNotFound(self):
        from NotFound import Ui_NotFound
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NotFound()
        self.ui.setupUi(self.window)
        self.window.show()

    def openResult(self,id):
        from Result import Ui_ResultPage
        result = db.child("csvTable").get()
        for res in result.each():
            if res.key() == id:

                self.result_name=res.val()['Name']
                self.result_loc=res.val()['Location'][0]
                self.result_date = res.val()['Location'][1]
                self.result_time=res.val()['Location'][2]
                self.result_cam_id=res.val()['Location'][3]

        self.window = QtWidgets.QDialog()
        self.ui = Ui_ResultPage()
        self.ui.setupUi(self.window,self.result_name,self.result_date,self.result_time,self.result_loc,self.result_cam_id ,id)
        self.window.show()

    def searchFunc(self):
        import firebasedb
        name = self.text_name.text()
        id = self.text_id.text()
        val = firebasedb.returnValues(id)
        if val:
            self.openResult(id)
        else:
            self.openNotFound()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 700)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label_bg = QtWidgets.QLabel(Dialog)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label_bg.setStyleSheet("background-image: url(:/newPrefix/BG-FB1.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(250, 540, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.search.setStyleSheet("QPushButton{\n"
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
        self.search.setObjectName("search")
        self.search.clicked.connect(self.searchFunc)

        self.text_name = QtWidgets.QLineEdit(Dialog)
        self.text_name.setGeometry(QtCore.QRect(380, 440, 140, 22))
        self.text_name.setObjectName("text_name")

        self.text_name.setPlaceholderText("ex: PRIYANSH VERMA")
        validate_name = QRegExpValidator(QRegExp(r"^[A-Z\" \"]*$"))
        self.text_name.setValidator(validate_name)

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 480, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 440, 65, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(47, 67, 195);\n"
                                   "color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 370, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(210, 280, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_1.setObjectName("label_1")
        self.text_id = QtWidgets.QLineEdit(Dialog)
        self.text_id.setGeometry(QtCore.QRect(380, 480, 140, 22))
        self.text_id.setObjectName("text_id")
        self.text_id.setPlaceholderText("ex: 0206cs181118")
        validate_id = QRegExpValidator(QRegExp(r'[0-9a-z]{12}'))
        self.text_id.setValidator(validate_id)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 240, 241, 131))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(47, 67, 195);\n"
                                   "color: rgb(9, 13, 84);")
        self.label_2.setObjectName("label_2")
        self.label_logo = QtWidgets.QLabel(Dialog)
        self.label_logo.setGeometry(QtCore.QRect(250, 110, 171, 151))
        self.label_logo.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(300, 590, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.exit.setStyleSheet("border-radius : 10;\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255,255,255);\n"
"")

        self.exit.setObjectName("exit")
        self.exit.setCheckable(True)
        self.exit.clicked.connect(self.clickme)



        #self.exit.clicked.connect(print("thread closed"))
        #self.exit.clicked.connect(mainthread.join())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def clickme(self):
        if self.exit.isChecked():
            print("Thread closed")
            mainthread.join()
            Dialog.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search.setText(_translate("Dialog", "FACE GRAB"))
        self.label_5.setText(_translate("Dialog", "ID:"))
        self.label_4.setText(_translate("Dialog", "NAME:"))
        self.label_3.setText(_translate("Dialog", "ENTER DETAILS : "))
        self.label_1.setText(_translate("Dialog", "FACE"))
        self.label_2.setText(_translate("Dialog", "GRAB"))
        self.exit.setText(_translate("Dialog", "EXIT"))

import imgs_search_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SearchPage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

