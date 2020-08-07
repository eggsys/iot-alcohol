# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outputtext.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql.cursors


class Ui_Form(object):

    def db(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='pymysql',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        email = self.text_name
        # email = "egg.rkt2@gmail.com"
        pwd = self.textX
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (email, pwd))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `users` order by id DESC"
                # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql)
                result = cursor.fetchmany(5)
                print(result)
        finally:
            connection.close()

    def input_text(self):
        self.textX = "DATA FROM RFID"


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        self.text_name = input("Please enter your text:\n")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 380, 171, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 380, 101, 71))
        self.label_2.setObjectName("label_2")
        self.input_text()
        self.label.setText(self.textX)
        self.label_2.setText(self.text_name)
        self.db()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.label.setText(_translate("Form", "TextLabel"))
        #self.label_2.setText(_translate("Form", "OUTPUT TEXT   : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
