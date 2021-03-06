# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 871, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.TODLOGO = QtWidgets.QWidget()
        self.TODLOGO.setObjectName("TODLOGO")
        self.bg_tod = QtWidgets.QLabel(self.TODLOGO)
        self.bg_tod.setGeometry(QtCore.QRect(-30, 0, 871, 561))
        self.bg_tod.setStyleSheet("background-image: url(:/bg1/1.gif);")
        self.bg_tod.setText("")
        self.bg_tod.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.bg_tod.setScaledContents(True)
        self.bg_tod.setObjectName("bg_tod")
        self.stackedWidget.addWidget(self.TODLOGO)
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.bg_welcome = QtWidgets.QLabel(self.Welcome)
        self.bg_welcome.setGeometry(QtCore.QRect(-30, -10, 871, 581))
        self.bg_welcome.setStyleSheet("background-image: url(:/newPrefix/02.jpg);")
        self.bg_welcome.setText("")
        self.bg_welcome.setPixmap(QtGui.QPixmap(":/newPrefix/02.jpg"))
        self.bg_welcome.setScaledContents(True)
        self.bg_welcome.setObjectName("bg_welcome")
        self.stackedWidget.addWidget(self.Welcome)
        self.usertype = QtWidgets.QWidget()
        self.usertype.setObjectName("usertype")
        self.bg_visitor = QtWidgets.QLabel(self.usertype)
        self.bg_visitor.setGeometry(QtCore.QRect(-10, 0, 851, 571))
        self.bg_visitor.setStyleSheet("background-image: url(:/bg2/00.jpg);")
        self.bg_visitor.setText("")
        self.bg_visitor.setPixmap(QtGui.QPixmap(":/bg2/00.jpg"))
        self.bg_visitor.setScaledContents(True)
        self.bg_visitor.setObjectName("bg_visitor")
        self.stackedWidget.addWidget(self.usertype)
        self.identype = QtWidgets.QWidget()
        self.identype.setObjectName("identype")
        self.bg_iden = QtWidgets.QLabel(self.identype)
        self.bg_iden.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.bg_iden.setStyleSheet("background-image: url(:/scan/03.gif);")
        self.bg_iden.setText("")
        self.bg_iden.setPixmap(QtGui.QPixmap(":/scan/03.gif"))
        self.bg_iden.setScaledContents(True)
        self.bg_iden.setObjectName("bg_iden")
        self.stackedWidget.addWidget(self.identype)
        self.fingerprint = QtWidgets.QWidget()
        self.fingerprint.setObjectName("fingerprint")
        self.bg = QtWidgets.QLabel(self.fingerprint)
        self.bg.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.bg.setStyleSheet("background-image: url(:/bg1/1.gif);")
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.icon_fingerprint = QtWidgets.QLabel(self.fingerprint)
        self.icon_fingerprint.setGeometry(QtCore.QRect(320, 210, 201, 211))
        self.icon_fingerprint.setStyleSheet("background-image: url(:/fingerprint/fingerprint-scanning-line-icon-vector-19563770.jpg);\n"
"background-color: rgb(255, 255, 255);")
        self.icon_fingerprint.setText("")
        self.icon_fingerprint.setPixmap(QtGui.QPixmap(":/fingerprint/fingerprint-scanning-line-icon-vector-19563770.jpg"))
        self.icon_fingerprint.setScaledContents(True)
        self.icon_fingerprint.setObjectName("icon_fingerprint")
        self.stackedWidget.addWidget(self.fingerprint)
        self.User_info = QtWidgets.QWidget()
        self.User_info.setObjectName("User_info")
        self.Emp_section = QtWidgets.QTextBrowser(self.User_info)
        self.Emp_section.setGeometry(QtCore.QRect(-20, 300, 821, 211))
        self.Emp_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.Emp_section.setObjectName("Emp_section")
        self.radio_out = QtWidgets.QRadioButton(self.User_info)
        self.radio_out.setGeometry(QtCore.QRect(80, 200, 81, 51))
        self.radio_out.setAcceptDrops(False)
        self.radio_out.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out.setChecked(False)
        self.radio_out.setObjectName("radio_out")
        self.device_section = QtWidgets.QTextBrowser(self.User_info)
        self.device_section.setGeometry(QtCore.QRect(0, 80, 821, 91))
        self.device_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section.setObjectName("device_section")
        self.Emp_name = QtWidgets.QLabel(self.User_info)
        self.Emp_name.setGeometry(QtCore.QRect(460, 90, 241, 61))
        self.Emp_name.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_name.setScaledContents(False)
        self.Emp_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_name.setIndent(0)
        self.Emp_name.setObjectName("Emp_name")
        self.DateandTime = QtWidgets.QTextBrowser(self.User_info)
        self.DateandTime.setGeometry(QtCore.QRect(0, 10, 821, 61))
        self.DateandTime.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime.setObjectName("DateandTime")
        self.radio_in = QtWidgets.QRadioButton(self.User_info)
        self.radio_in.setGeometry(QtCore.QRect(0, 200, 81, 51))
        self.radio_in.setAcceptDrops(False)
        self.radio_in.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in.setChecked(False)
        self.radio_in.setObjectName("radio_in")
        self.Dept = QtWidgets.QTextBrowser(self.User_info)
        self.Dept.setGeometry(QtCore.QRect(400, 180, 331, 81))
        self.Dept.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Dept.setObjectName("Dept")
        self.Emp_pic = QtWidgets.QLabel(self.User_info)
        self.Emp_pic.setGeometry(QtCore.QRect(10, 340, 171, 161))
        self.Emp_pic.setStyleSheet("image: url(:/image/users-vector-icon-png_260862.jpg);")
        self.Emp_pic.setText("")
        self.Emp_pic.setObjectName("Emp_pic")
        self.Emp_message = QtWidgets.QLabel(self.User_info)
        self.Emp_message.setGeometry(QtCore.QRect(230, 420, 321, 71))
        self.Emp_message.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_message.setScaledContents(False)
        self.Emp_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_message.setIndent(0)
        self.Emp_message.setObjectName("Emp_message")
        self.bg_2 = QtWidgets.QLabel(self.User_info)
        self.bg_2.setGeometry(QtCore.QRect(0, 0, 841, 561))
        self.bg_2.setStyleSheet("background-color: rgb(66, 164, 255);")
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")
        self.device_type = QtWidgets.QLabel(self.User_info)
        self.device_type.setGeometry(QtCore.QRect(190, 100, 161, 41))
        self.device_type.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.device_type.setObjectName("device_type")
        self.bg_2.raise_()
        self.Emp_section.raise_()
        self.radio_out.raise_()
        self.device_section.raise_()
        self.Emp_name.raise_()
        self.DateandTime.raise_()
        self.radio_in.raise_()
        self.Dept.raise_()
        self.Emp_pic.raise_()
        self.Emp_message.raise_()
        self.device_type.raise_()
        self.stackedWidget.addWidget(self.User_info)
        self.blow = QtWidgets.QWidget()
        self.blow.setObjectName("blow")
        self.bg_blow = QtWidgets.QLabel(self.blow)
        self.bg_blow.setGeometry(QtCore.QRect(0, 0, 841, 561))
        self.bg_blow.setStyleSheet("\n"
"background-image: url(:/blow/05.gif);")
        self.bg_blow.setText("")
        self.bg_blow.setPixmap(QtGui.QPixmap(":/blow/05.gif"))
        self.bg_blow.setScaledContents(True)
        self.bg_blow.setObjectName("bg_blow")
        self.stackedWidget.addWidget(self.blow)
        self.User_result = QtWidgets.QWidget()
        self.User_result.setObjectName("User_result")
        self.label_5 = QtWidgets.QLabel(self.User_result)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 841, 561))
        self.label_5.setStyleSheet("background-color: rgb(66, 164, 255);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.Dateandtime = QtWidgets.QTextBrowser(self.User_result)
        self.Dateandtime.setGeometry(QtCore.QRect(10, 10, 821, 61))
        self.Dateandtime.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.Dateandtime.setObjectName("Dateandtime")
        self.device_section_2 = QtWidgets.QTextBrowser(self.User_result)
        self.device_section_2.setGeometry(QtCore.QRect(10, 80, 821, 91))
        self.device_section_2.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section_2.setObjectName("device_section_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.User_result)
        self.textBrowser_3.setGeometry(QtCore.QRect(-10, 300, 821, 211))
        self.textBrowser_3.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.Dept_2 = QtWidgets.QTextBrowser(self.User_result)
        self.Dept_2.setGeometry(QtCore.QRect(410, 180, 331, 81))
        self.Dept_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Dept_2.setObjectName("Dept_2")
        self.Emp_pic_2 = QtWidgets.QLabel(self.User_result)
        self.Emp_pic_2.setGeometry(QtCore.QRect(20, 340, 171, 161))
        self.Emp_pic_2.setStyleSheet("image: url(:/image/users-vector-icon-png_260862.jpg);")
        self.Emp_pic_2.setText("")
        self.Emp_pic_2.setObjectName("Emp_pic_2")
        self.Emp_name_2 = QtWidgets.QLabel(self.User_result)
        self.Emp_name_2.setGeometry(QtCore.QRect(450, 90, 241, 61))
        self.Emp_name_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_name_2.setScaledContents(False)
        self.Emp_name_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_name_2.setIndent(0)
        self.Emp_name_2.setObjectName("Emp_name_2")
        self.device_type_2 = QtWidgets.QLabel(self.User_result)
        self.device_type_2.setGeometry(QtCore.QRect(200, 103, 161, 41))
        self.device_type_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.device_type_2.setObjectName("device_type_2")
        self.result_Alch = QtWidgets.QLabel(self.User_result)
        self.result_Alch.setGeometry(QtCore.QRect(220, 320, 141, 71))
        self.result_Alch.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.result_Alch.setText("")
        self.result_Alch.setObjectName("result_Alch")
        self.result_temp = QtWidgets.QLabel(self.User_result)
        self.result_temp.setGeometry(QtCore.QRect(390, 320, 161, 71))
        self.result_temp.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.result_temp.setText("")
        self.result_temp.setObjectName("result_temp")
        self.Emp_message_2 = QtWidgets.QLabel(self.User_result)
        self.Emp_message_2.setGeometry(QtCore.QRect(220, 420, 321, 71))
        self.Emp_message_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_message_2.setScaledContents(False)
        self.Emp_message_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_message_2.setIndent(0)
        self.Emp_message_2.setObjectName("Emp_message_2")
        self.radio_in_2 = QtWidgets.QRadioButton(self.User_result)
        self.radio_in_2.setGeometry(QtCore.QRect(10, 200, 81, 51))
        self.radio_in_2.setAcceptDrops(False)
        self.radio_in_2.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in_2.setChecked(False)
        self.radio_in_2.setObjectName("radio_in_2")
        self.radio_out_2 = QtWidgets.QRadioButton(self.User_result)
        self.radio_out_2.setGeometry(QtCore.QRect(90, 200, 81, 51))
        self.radio_out_2.setAcceptDrops(False)
        self.radio_out_2.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out_2.setChecked(False)
        self.radio_out_2.setObjectName("radio_out_2")
        self.stackedWidget.addWidget(self.User_result)
        self.clean = QtWidgets.QWidget()
        self.clean.setObjectName("clean")
        self.bg_3 = QtWidgets.QLabel(self.clean)
        self.bg_3.setGeometry(QtCore.QRect(0, 0, 841, 561))
        self.bg_3.setStyleSheet("background-image: url(:/bg1/1.gif);")
        self.bg_3.setText("")
        self.bg_3.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.bg_3.setScaledContents(True)
        self.bg_3.setObjectName("bg_3")
        self.message = QtWidgets.QLabel(self.clean)
        self.message.setGeometry(QtCore.QRect(90, 180, 731, 251))
        self.message.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.message.setScaledContents(False)
        self.message.setObjectName("message")
        self.stackedWidget.addWidget(self.clean)
        self.User_pass = QtWidgets.QWidget()
        self.User_pass.setObjectName("User_pass")
        self.bg_4 = QtWidgets.QLabel(self.User_pass)
        self.bg_4.setGeometry(QtCore.QRect(0, 0, 841, 561))
        self.bg_4.setStyleSheet("background-color: rgb(66, 164, 255);")
        self.bg_4.setText("")
        self.bg_4.setPixmap(QtGui.QPixmap(":/bg1/1.gif"))
        self.bg_4.setScaledContents(True)
        self.bg_4.setObjectName("bg_4")
        self.DateandTime_2 = QtWidgets.QTextBrowser(self.User_pass)
        self.DateandTime_2.setGeometry(QtCore.QRect(10, 10, 821, 61))
        self.DateandTime_2.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime_2.setObjectName("DateandTime_2")
        self.device_section_3 = QtWidgets.QTextBrowser(self.User_pass)
        self.device_section_3.setGeometry(QtCore.QRect(10, 90, 821, 91))
        self.device_section_3.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section_3.setObjectName("device_section_3")
        self.emp_section = QtWidgets.QTextBrowser(self.User_pass)
        self.emp_section.setGeometry(QtCore.QRect(10, 290, 821, 211))
        self.emp_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.emp_section.setObjectName("emp_section")
        self.emp_pic = QtWidgets.QLabel(self.User_pass)
        self.emp_pic.setGeometry(QtCore.QRect(30, 320, 171, 161))
        self.emp_pic.setStyleSheet("image: url(:/image/users-vector-icon-png_260862.jpg);")
        self.emp_pic.setText("")
        self.emp_pic.setObjectName("emp_pic")
        self.result_temp_2 = QtWidgets.QLabel(self.User_pass)
        self.result_temp_2.setGeometry(QtCore.QRect(400, 320, 161, 71))
        self.result_temp_2.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.result_temp_2.setText("")
        self.result_temp_2.setObjectName("result_temp_2")
        self.result_alch = QtWidgets.QLabel(self.User_pass)
        self.result_alch.setGeometry(QtCore.QRect(230, 320, 141, 71))
        self.result_alch.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.result_alch.setText("")
        self.result_alch.setObjectName("result_alch")
        self.emp_message = QtWidgets.QLabel(self.User_pass)
        self.emp_message.setGeometry(QtCore.QRect(230, 410, 321, 71))
        self.emp_message.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.emp_message.setScaledContents(False)
        self.emp_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emp_message.setIndent(0)
        self.emp_message.setObjectName("emp_message")
        self.dept = QtWidgets.QTextBrowser(self.User_pass)
        self.dept.setGeometry(QtCore.QRect(430, 190, 331, 81))
        self.dept.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.dept.setObjectName("dept")
        self.PASS = QtWidgets.QLabel(self.User_pass)
        self.PASS.setGeometry(QtCore.QRect(210, 170, 241, 121))
        self.PASS.setStyleSheet("color: rgb(85, 255, 0);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"")
        self.PASS.setObjectName("PASS")
        self.radio_in_3 = QtWidgets.QRadioButton(self.User_pass)
        self.radio_in_3.setGeometry(QtCore.QRect(10, 200, 81, 51))
        self.radio_in_3.setAcceptDrops(False)
        self.radio_in_3.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in_3.setChecked(False)
        self.radio_in_3.setObjectName("radio_in_3")
        self.radio_out_3 = QtWidgets.QRadioButton(self.User_pass)
        self.radio_out_3.setGeometry(QtCore.QRect(90, 200, 81, 51))
        self.radio_out_3.setAcceptDrops(False)
        self.radio_out_3.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out_3.setChecked(False)
        self.radio_out_3.setObjectName("radio_out_3")
        self.stackedWidget.addWidget(self.User_pass)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(9)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Emp_section.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radio_out.setText(_translate("MainWindow", "Out"))
        self.device_section.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.Emp_name.setText(_translate("MainWindow", "Emp_Name"))
        self.DateandTime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.radio_in.setText(_translate("MainWindow", "In"))
        self.Dept.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.Emp_message.setText(_translate("MainWindow", "Emp_Message"))
        self.device_type.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Device_type</span></p></body></html>"))
        self.device_type.setText(_translate("MainWindow", "Device_type"))
        self.Dateandtime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.device_section_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Dept_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.Emp_name_2.setText(_translate("MainWindow", "Emp_Name"))
        self.device_type_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Device_type</span></p></body></html>"))
        self.device_type_2.setText(_translate("MainWindow", "Device_type"))
        self.Emp_message_2.setText(_translate("MainWindow", "Emp_Message"))
        self.radio_in_2.setText(_translate("MainWindow", "In"))
        self.radio_out_2.setText(_translate("MainWindow", "Out"))
        self.message.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">กรุณาล้างมือด้วย</span></p><p><span style=\" color:#ffffff;\">แอลกอฮอล์ด้านล่าง</span></p></body></html>"))
        self.message.setText(_translate("MainWindow", "กรุณาล้างมือด้วยแอลกอฮอลข้างล่าง"))
        self.DateandTime_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.device_section_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.emp_section.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.emp_message.setText(_translate("MainWindow", "Emp_Message"))
        self.dept.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.PASS.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55ff7f;\">PASS</span></p></body></html>"))
        self.PASS.setText(_translate("MainWindow", "Pass"))
        self.radio_in_3.setText(_translate("MainWindow", "In"))
        self.radio_out_3.setText(_translate("MainWindow", "Out"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
