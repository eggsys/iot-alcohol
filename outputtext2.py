# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outputtext2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql.cursors
from datetime import datetime
import time

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
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)

        self.text_name = input("Please enter your text:\n")

        self.input_text()
        self.label_bg6 = QtWidgets.QLabel(Form)
        self.label_bg6.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg6.setText("")
        self.label_bg6.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg6.setScaledContents(True)
        self.label_bg6.setObjectName("label_bg6")
        self.device_section = QtWidgets.QTextBrowser(Form)
        self.device_section.setGeometry(QtCore.QRect(60, 120, 821, 91))
        self.device_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section.setObjectName("device_section")
        self.DateandTime = QtWidgets.QTextBrowser(Form)
        self.DateandTime.setGeometry(QtCore.QRect(60, 50, 821, 61))
        self.DateandTime.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime.setObjectName("DateandTime")
        self.DateandTime.setText(self.current_time)
        self.Emp_section = QtWidgets.QTextBrowser(Form)
        self.Emp_section.setGeometry(QtCore.QRect(40, 340, 821, 211))
        self.Emp_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.Emp_section.setObjectName("Emp_section")
        self.radio_out = QtWidgets.QRadioButton(Form)
        self.radio_out.setGeometry(QtCore.QRect(140, 240, 81, 51))
        self.radio_out.setAcceptDrops(False)
        self.radio_out.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out.setChecked(False)
        self.radio_out.setObjectName("radio_out")
        self.Dept = QtWidgets.QTextBrowser(Form)
        self.Dept.setGeometry(QtCore.QRect(460, 220, 331, 81))
        self.Dept.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Dept.setObjectName("Dept")
        self.Emp_message = QtWidgets.QLabel(Form)
        self.Emp_message.setGeometry(QtCore.QRect(320, 450, 321, 71))
        self.Emp_message.setText("  We got some Message for you ")
        self.Emp_message.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_message.setScaledContents(False)
        self.Emp_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_message.setIndent(0)
        self.Emp_message.setObjectName("Emp_message")
        self.label_portrait = QtWidgets.QLabel(Form)
        self.label_portrait.setGeometry(QtCore.QRect(80, 370, 151, 151))
        self.label_portrait.setText("")
        self.label_portrait.setPixmap(QtGui.QPixmap("users-vector-icon-png_260862.jpg"))
        self.label_portrait.setScaledContents(True)
        self.label_portrait.setObjectName("label_portrait")
        self.radio_in = QtWidgets.QRadioButton(Form)
        self.radio_in.setGeometry(QtCore.QRect(60, 240, 81, 51))
        self.radio_in.setAcceptDrops(False)
        self.radio_in.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in.setChecked(False)
        self.radio_in.setObjectName("radio_in")
        self.label_datetime = QtWidgets.QLabel(Form)
        self.label_datetime.setGeometry(QtCore.QRect(440, 60, 221, 41))
        self.label_datetime.setObjectName("label_datetime")
        self.label_datetime.setText(self.text_name)
        self.label_datetime.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n")
        self.label_device = QtWidgets.QLabel(Form)
        self.label_device.setGeometry(QtCore.QRect(440, 150, 400, 41))
        self.label_device.setObjectName("label_device")

        self.db()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.device_section.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))

        #self.DateandTime.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
##"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"#))

        self.Emp_section.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radio_out.setText(_translate("Form", "Out"))
        self.Dept.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        #self.Emp_message.setText(_translate("Form", "Emp_Message"))
        self.radio_in.setText(_translate("Form", "In"))
      #  self.label_datetime.setText(_translate("Form", "TextLabel"))
        self.label_device.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
