# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_Form(object):
#button functions
    def clicked_back(self, nd):
        print("click : go back")
        Form.pageX = - 1

    def clicked(self):
        print(Form.pageX)
        print("click : go Next")
        Form.pageX +=  1
        print(Form.pageX)

        self.stackedWidget.setCurrentIndex(Form.pageX)

    def clicked_end(self):
        print(Form.pageX)
        print("click end button")
        Form.pageX = 0
        print(Form.pageX)
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1021, 600)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_bg1 = QtWidgets.QLabel(self.page)
        self.label_bg1.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label_bg1.setText("")
        self.label_bg1.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg1.setScaledContents(True)
        self.label_bg1.setObjectName("label_bg1")

        self.Button_01 = QtWidgets.QPushButton(self.page)
        self.Button_01.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.Button_01.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_01.setText("")
        self.Button_01.setObjectName("Button_01")
        self.Button_01.clicked.connect(self.clicked)


        self.stackedWidget.addWidget(self.page)


        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_bg2 = QtWidgets.QLabel(self.page_2)
        self.label_bg2.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg2.setText("")
        self.label_bg2.setPixmap(QtGui.QPixmap("02.jpg"))
        self.label_bg2.setScaledContents(True)
        self.label_bg2.setObjectName("label_bg2")
        self.Button_2 = QtWidgets.QPushButton(self.page_2)
        self.Button_2.setGeometry(QtCore.QRect(760, 480, 201, 61))
        self.Button_2.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_2.setText("")
        self.Button_2.setObjectName("Button_2")
        self.Button_2.clicked.connect(self.clicked)


        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_bg3 = QtWidgets.QLabel(self.page_3)
        self.label_bg3.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg3.setText("")
        self.label_bg3.setPixmap(QtGui.QPixmap("00.jpg"))
        self.label_bg3.setScaledContents(True)
        self.label_bg3.setObjectName("label_bg3")
        self.Button_3 = QtWidgets.QPushButton(self.page_3)
        self.Button_3.setGeometry(QtCore.QRect(80, 220, 381, 131))
        self.Button_3.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_3.setText("")
        self.Button_3.setObjectName("Button_3")
        self.Button_3.clicked.connect(self.clicked)

        self.Button_4 = QtWidgets.QPushButton(self.page_3)
        self.Button_4.setGeometry(QtCore.QRect(570, 220, 371, 131))
        self.Button_4.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_4.setText("")
        self.Button_4.setObjectName("Button_4")
        self.Button_4.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_3)


        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")

        self.label_bg4 = QtWidgets.QLabel(self.page_4)
        self.label_bg4.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg4.setText("")

        #self.label_bg4.setPixmap(QtGui.QPixmap("03.gif"))
        self.gif = QMovie('03.gif')
        self.label_bg4.setMovie(self.gif)
        self.gif.start()
        self.label_bg4.setScaledContents(True)
        self.label_bg4.setObjectName("label_bg4")


        self.Button_5 = QtWidgets.QPushButton(self.page_4)
        self.Button_5.setGeometry(QtCore.QRect(580, 60, 381, 131))
        self.Button_5.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_5.setText("")
        self.Button_5.setObjectName("Button_5")
        self.Button_5.clicked.connect(self.clicked)

        self.Button_6 = QtWidgets.QPushButton(self.page_4)
        self.Button_6.setGeometry(QtCore.QRect(590, 410, 381, 131))
        self.Button_6.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_6.setText("")
        self.Button_6.setObjectName("Button_6")
        self.Button_6.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_4)




        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_bg5 = QtWidgets.QLabel(self.page_5)
        self.label_bg5.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg5.setText("")
        self.label_bg5.setPixmap(QtGui.QPixmap("3161227.jpg"))
        self.label_bg5.setScaledContents(True)
        self.label_bg5.setObjectName("label_bg5")
        self.Button_7 = QtWidgets.QPushButton(self.page_5)
        self.Button_7.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.Button_7.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_7.setText("")
        self.Button_7.setObjectName("Button_7")
        self.Button_7.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_5)


        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_bg6 = QtWidgets.QLabel(self.page_6)
        self.label_bg6.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg6.setText("")
        self.label_bg6.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg6.setScaledContents(True)
        self.label_bg6.setObjectName("label_bg6")
        self.device_type = QtWidgets.QLabel(self.page_6)
        self.device_type.setGeometry(QtCore.QRect(250, 140, 161, 41))
        self.device_type.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.device_type.setObjectName("device_type")
        self.radio_out = QtWidgets.QRadioButton(self.page_6)
        self.radio_out.setGeometry(QtCore.QRect(140, 240, 81, 51))
        self.radio_out.setAcceptDrops(False)
        self.radio_out.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out.setChecked(False)
        self.radio_out.setObjectName("radio_out")
        self.DateandTime = QtWidgets.QTextBrowser(self.page_6)
        self.DateandTime.setGeometry(QtCore.QRect(60, 50, 821, 61))
        self.DateandTime.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime.setObjectName("DateandTime")
        self.device_section = QtWidgets.QTextBrowser(self.page_6)
        self.device_section.setGeometry(QtCore.QRect(60, 120, 821, 91))
        self.device_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section.setObjectName("device_section")
        self.Emp_name = QtWidgets.QLabel(self.page_6)
        self.Emp_name.setGeometry(QtCore.QRect(520, 130, 241, 61))
        self.Emp_name.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_name.setScaledContents(False)
        self.Emp_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_name.setIndent(0)
        self.Emp_name.setObjectName("Emp_name")
        self.radio_in = QtWidgets.QRadioButton(self.page_6)
        self.radio_in.setGeometry(QtCore.QRect(60, 240, 81, 51))
        self.radio_in.setAcceptDrops(False)
        self.radio_in.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in.setChecked(False)
        self.radio_in.setObjectName("radio_in")
        self.Dept = QtWidgets.QTextBrowser(self.page_6)
        self.Dept.setGeometry(QtCore.QRect(460, 220, 331, 81))
        self.Dept.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Dept.setObjectName("Dept")
        self.Emp_section = QtWidgets.QTextBrowser(self.page_6)
        self.Emp_section.setGeometry(QtCore.QRect(40, 340, 821, 211))
        self.Emp_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.Emp_section.setObjectName("Emp_section")
        self.label = QtWidgets.QLabel(self.page_6)
        self.label.setGeometry(QtCore.QRect(60, 370, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("users-vector-icon-png_260862.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Emp_message = QtWidgets.QLabel(self.page_6)
        self.Emp_message.setGeometry(QtCore.QRect(280, 440, 321, 71))
        self.Emp_message.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_message.setScaledContents(False)
        self.Emp_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_message.setIndent(0)
        self.Emp_message.setObjectName("Emp_message")
        self.Button_8 = QtWidgets.QPushButton(self.page_6)
        self.Button_8.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.Button_8.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_8.setText("")
        self.Button_8.setObjectName("Button_8")
        self.Button_8.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_6)


        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")


        self.label_bg7 = QtWidgets.QLabel(self.page_7)
        self.label_bg7.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg7.setText("")
        #self.label_bg7.setPixmap(QtGui.QPixmap("05.gif"))
        self.gif = QMovie('05.gif')
        self.label_bg7.setMovie(self.gif)
        self.gif.start()
        self.label_bg7.setScaledContents(True)
        self.label_bg7.setObjectName("label_bg7")


        self.Button_9 = QtWidgets.QPushButton(self.page_7)
        self.Button_9.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.Button_9.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_9.setText("")
        self.Button_9.setObjectName("Button_9")
        self.Button_9.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_7)


        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_bg8 = QtWidgets.QLabel(self.page_8)
        self.label_bg8.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg8.setText("")
        self.label_bg8.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg8.setScaledContents(True)
        self.label_bg8.setObjectName("label_bg8")
        self.Emp_section_2 = QtWidgets.QTextBrowser(self.page_8)
        self.Emp_section_2.setGeometry(QtCore.QRect(70, 340, 821, 211))
        self.Emp_section_2.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.Emp_section_2.setObjectName("Emp_section_2")
        self.radio_out_2 = QtWidgets.QRadioButton(self.page_8)
        self.radio_out_2.setGeometry(QtCore.QRect(170, 240, 81, 51))
        self.radio_out_2.setAcceptDrops(False)
        self.radio_out_2.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out_2.setChecked(False)
        self.radio_out_2.setObjectName("radio_out_2")
        self.Emp_message_2 = QtWidgets.QLabel(self.page_8)
        self.Emp_message_2.setGeometry(QtCore.QRect(310, 440, 321, 71))
        self.Emp_message_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.Emp_message_2.setScaledContents(False)
        self.Emp_message_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Emp_message_2.setIndent(0)
        self.Emp_message_2.setObjectName("Emp_message_2")
        self.label_2 = QtWidgets.QLabel(self.page_8)
        self.label_2.setGeometry(QtCore.QRect(90, 370, 151, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("users-vector-icon-png_260862.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.device_section_2 = QtWidgets.QTextBrowser(self.page_8)
        self.device_section_2.setGeometry(QtCore.QRect(90, 120, 821, 91))
        self.device_section_2.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section_2.setObjectName("device_section_2")
        self.DateandTime_2 = QtWidgets.QTextBrowser(self.page_8)
        self.DateandTime_2.setGeometry(QtCore.QRect(90, 50, 821, 61))
        self.DateandTime_2.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime_2.setObjectName("DateandTime_2")
        self.Dept_2 = QtWidgets.QTextBrowser(self.page_8)
        self.Dept_2.setGeometry(QtCore.QRect(490, 220, 331, 81))
        self.Dept_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Dept_2.setObjectName("Dept_2")
        self.radio_in_2 = QtWidgets.QRadioButton(self.page_8)
        self.radio_in_2.setGeometry(QtCore.QRect(90, 240, 81, 51))
        self.radio_in_2.setAcceptDrops(False)
        self.radio_in_2.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in_2.setChecked(False)
        self.radio_in_2.setObjectName("radio_in_2")
        self.result_Alch = QtWidgets.QLabel(self.page_8)
        self.result_Alch.setGeometry(QtCore.QRect(290, 360, 141, 71))
        self.result_Alch.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.result_Alch.setText("")
        self.result_Alch.setObjectName("result_Alch")
        self.result_temp = QtWidgets.QLabel(self.page_8)
        self.result_temp.setGeometry(QtCore.QRect(460, 360, 161, 71))
        self.result_temp.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.result_temp.setText("")
        self.result_temp.setObjectName("result_temp")
        self.Button_10 = QtWidgets.QPushButton(self.page_8)
        self.Button_10.setGeometry(QtCore.QRect(-10, 0, 1024, 600))
        self.Button_10.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_10.setText("")
        self.Button_10.setObjectName("Button_10")
        self.Button_10.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_8)



        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_bg9 = QtWidgets.QLabel(self.page_9)
        self.label_bg9.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg9.setText("")
        self.label_bg9.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg9.setScaledContents(True)
        self.label_bg9.setObjectName("label_bg9")
        self.message = QtWidgets.QLabel(self.page_9)
        self.message.setGeometry(QtCore.QRect(170, 180, 731, 251))
        self.message.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.message.setScaledContents(False)
        self.message.setObjectName("message")
        self.Button_11 = QtWidgets.QPushButton(self.page_9)
        self.Button_11.setGeometry(QtCore.QRect(-10, 0, 1024, 600))
        self.Button_11.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 00%)")
        self.Button_11.setText("")
        self.Button_11.setObjectName("Button_11")
        self.Button_11.clicked.connect(self.clicked)
        self.stackedWidget.addWidget(self.page_9)


        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_bg10 = QtWidgets.QLabel(self.page_10)
        self.label_bg10.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg10.setText("")
        self.label_bg10.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg10.setScaledContents(True)
        self.label_bg10.setObjectName("label_bg10")
        self.DateandTime_3 = QtWidgets.QTextBrowser(self.page_10)
        self.DateandTime_3.setGeometry(QtCore.QRect(40, 50, 821, 61))
        self.DateandTime_3.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.DateandTime_3.setObjectName("DateandTime_3")
        self.radio_in_3 = QtWidgets.QRadioButton(self.page_10)
        self.radio_in_3.setGeometry(QtCore.QRect(40, 240, 81, 51))
        self.radio_in_3.setAcceptDrops(False)
        self.radio_in_3.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_in_3.setChecked(False)
        self.radio_in_3.setObjectName("radio_in_3")
        self.PASS = QtWidgets.QLabel(self.page_10)
        self.PASS.setGeometry(QtCore.QRect(240, 210, 241, 121))
        self.PASS.setStyleSheet("color: rgb(85, 255, 0);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"")
        self.PASS.setObjectName("PASS")
        self.dept = QtWidgets.QTextBrowser(self.page_10)
        self.dept.setGeometry(QtCore.QRect(460, 230, 331, 81))
        self.dept.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.dept.setObjectName("dept")
        self.device_section_3 = QtWidgets.QTextBrowser(self.page_10)
        self.device_section_3.setGeometry(QtCore.QRect(40, 130, 821, 91))
        self.device_section_3.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.device_section_3.setObjectName("device_section_3")
        self.radio_out_3 = QtWidgets.QRadioButton(self.page_10)
        self.radio_out_3.setGeometry(QtCore.QRect(120, 240, 81, 51))
        self.radio_out_3.setAcceptDrops(False)
        self.radio_out_3.setStyleSheet("background-color: rgb(29, 80, 109);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.radio_out_3.setChecked(False)
        self.radio_out_3.setObjectName("radio_out_3")
        self.emp_section = QtWidgets.QTextBrowser(self.page_10)
        self.emp_section.setGeometry(QtCore.QRect(40, 330, 821, 211))
        self.emp_section.setStyleSheet("\n"
"background-color: rgb(29, 80, 109);")
        self.emp_section.setObjectName("emp_section")
        self.result_temp_2 = QtWidgets.QLabel(self.page_10)
        self.result_temp_2.setGeometry(QtCore.QRect(410, 350, 161, 71))
        self.result_temp_2.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.result_temp_2.setText("")
        self.result_temp_2.setObjectName("result_temp_2")
        self.result_alch = QtWidgets.QLabel(self.page_10)
        self.result_alch.setGeometry(QtCore.QRect(240, 350, 141, 71))
        self.result_alch.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.result_alch.setText("")
        self.result_alch.setObjectName("result_alch")
        self.emp_message = QtWidgets.QLabel(self.page_10)
        self.emp_message.setGeometry(QtCore.QRect(240, 440, 321, 71))
        self.emp_message.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.emp_message.setScaledContents(False)
        self.emp_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emp_message.setIndent(0)
        self.emp_message.setObjectName("emp_message")
        self.label_3 = QtWidgets.QLabel(self.page_10)
        self.label_3.setGeometry(QtCore.QRect(60, 360, 161, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("users-vector-icon-png_260862.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.Button_12 = QtWidgets.QPushButton(self.page_10)
        self.Button_12.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.Button_12.setStyleSheet("\n"
"background-color : rgba(0, 0, 0, 0%)")
        self.Button_12.setText("")
        self.Button_12.setObjectName("Button_12")
        self.Button_12.clicked.connect(self.clicked_end)
        self.stackedWidget.addWidget(self.page_10)

        Form.pageX = 0
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(Form.pageX)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.device_type.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt;\">Device_type</span></p></body></html>"))
        self.device_type.setText(_translate("Form", "Device_type"))
        self.radio_out.setText(_translate("Form", "Out"))
        self.DateandTime.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.device_section.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.Emp_name.setText(_translate("Form", "Emp_Name"))
        self.radio_in.setText(_translate("Form", "In"))
        self.Dept.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.Emp_section.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Emp_message.setText(_translate("Form", "Emp_Message"))
        self.Emp_section_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radio_out_2.setText(_translate("Form", "Out"))
        self.Emp_message_2.setText(_translate("Form", "Emp_Message"))
        self.device_section_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.DateandTime_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.Dept_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.radio_in_2.setText(_translate("Form", "In"))
        self.message.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">กรุณาล้างมือด้วย</span></p><p><span style=\" color:#ffffff;\">แอลกอฮอล์ด้านล่าง</span></p></body></html>"))
        self.message.setText(_translate("Form", "กรุณาล้างมือด้วยแอลกอฮอลข้างล่าง"))
        self.DateandTime_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff;\">01/15/2020      08:40</span></p></body></html>"))
        self.radio_in_3.setText(_translate("Form", "In"))
        self.PASS.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" color:#55ff7f;\">PASS</span></p></body></html>"))
        self.PASS.setText(_translate("Form", "Pass"))
        self.dept.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Dept  : Accounting </span></p></body></html>"))
        self.device_section_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Device Type</span></p></body></html>"))
        self.radio_out_3.setText(_translate("Form", "Out"))
        self.emp_section.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.emp_message.setText(_translate("Form", "Emp_Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
