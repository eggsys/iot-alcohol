# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_withlabel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from datetime import datetime
import time

current_milli_time = lambda: int(round(time.time() * 1000))
now = datetime.now()

class Ui_Form(object):

    def event_screen1(self, event):

        Form.pageX += 1
        self.stackedWidget.setCurrentIndex(Form.pageX)
        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        millis = int(round(time.time() * 1000))
        print(current_time ,millis ,"Screen 1 : Welcome >> click")

        self.event_extra()

    def event_extra(self):
        current_time = now.strftime("%H:%M:%S")
        millis = int(round(time.time() * 1000))
        print(current_time ,millis , "Extra")


    def event_screen2_1(self, event):
        print("Screen 2 : LANG >> click TH")
        Form.pageX = 2
        self.stackedWidget.setCurrentIndex(Form.pageX)


    def event_screen2_2(self, event):
        print("Screen 2 : LANG >> click EN")
        Form.pageX = 2
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen3_1(self, event):
        print("Screen 3 : Visitor / Emp >> click Visitor")
        Form.pageX = 3
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen3_2(self, event):
        print("Screen 3 : Visitor / Emp >> click Employee")
        Form.pageX = 3
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen4_1(self, event):
        print("Screen 4 : IDEN click >> SCAN1.gif")
        Form.pageX = 4
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen4_2(self, event):
        print("Screen 4 : IDEN click >> SCAN2.gif")
        Form.pageX = 4
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen5(self, event):
        print("Screen 5 : FINGER PRINT >> click background")
        Form.pageX = 5
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen6(self, event):
        print("Screen 6 : EMP INFO  >> click background")
        Form.pageX = 6
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen7(self, event):
        print("Screen 7 : BLOW >> click background.GIF")
        Form.pageX = 7
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen8(self, event):
        print("Screen 8 : EMP Result >> click background")
        Form.pageX = 8
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen9(self, event):
        print("Screen 9 : Wash >> click background")
        Form.pageX = 9
        self.stackedWidget.setCurrentIndex(Form.pageX)

    def event_screen10(self, event):
        print("Screen 10 : Wash >> Result click background")
        Form.pageX = 0
        self.stackedWidget.setCurrentIndex(Form.pageX)



    def setupUi(self, Form):

        ## Window Screen size 1024 x 600
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1024, 600)

        ## Stack widget
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        ## PAGE 1
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_bg1 = QtWidgets.QLabel(self.page)
        self.label_bg1.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label_bg1.setText("")
        self.label_bg1.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg1.setScaledContents(True)
        self.label_bg1.setObjectName("label_bg1")
        self.label_bg1.mousePressEvent = self.event_screen1
        self.stackedWidget.addWidget(self.page)





        ## PAGE 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_bg2 = QtWidgets.QLabel(self.page_2)
        self.label_bg2.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg2.setText("")
        self.label_bg2.setPixmap(QtGui.QPixmap("02.jpg"))
        self.label_bg2.setScaledContents(True)
        self.label_bg2.setObjectName("label_bg2")

        self.label_buttonTH = QtWidgets.QLabel(self.page_2)
        self.label_buttonTH.setGeometry(QtCore.QRect(760, 480, 91, 61))
        self.label_buttonTH.setText("")
        self.label_buttonTH.setPixmap(QtGui.QPixmap("02-th.jpg"))
        self.label_buttonTH.setScaledContents(True)
        self.label_buttonTH.setObjectName("label_buttonTH")
        self.label_buttonTH.mousePressEvent = self.event_screen2_1

        self.label_buttonEN = QtWidgets.QLabel(self.page_2)
        self.label_buttonEN.setGeometry(QtCore.QRect(870, 480, 91, 61))
        self.label_buttonEN.setText("")
        self.label_buttonEN.setPixmap(QtGui.QPixmap("02-eng.jpg"))
        self.label_buttonEN.setScaledContents(True)
        self.label_buttonEN.setObjectName("label_buttonEN")
        self.label_buttonEN.mousePressEvent = self.event_screen2_2
        self.stackedWidget.addWidget(self.page_2)



        ## PAGE 3
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.label_bg3 = QtWidgets.QLabel(self.page_3)
        self.label_bg3.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg3.setText("")
        self.label_bg3.setPixmap(QtGui.QPixmap("00.jpg"))
        self.label_bg3.setScaledContents(True)
        self.label_bg3.setObjectName("label_bg3")

        self.label_ButttonVis = QtWidgets.QLabel(self.page_3)
        self.label_ButttonVis.setGeometry(QtCore.QRect(80, 220, 371, 121))
        self.label_ButttonVis.setText("")
        self.label_ButttonVis.setPixmap(QtGui.QPixmap("00-Visitor.jpg"))
        self.label_ButttonVis.setScaledContents(True)
        self.label_ButttonVis.setObjectName("label_ButttonVis")
        self.label_ButttonVis.mousePressEvent = self.event_screen3_1

        self.label_ButtonEmp = QtWidgets.QLabel(self.page_3)
        self.label_ButtonEmp.setGeometry(QtCore.QRect(570, 220, 371, 121))
        self.label_ButtonEmp.setText("")
        self.label_ButtonEmp.setPixmap(QtGui.QPixmap("00-Emp.jpg"))
        self.label_ButtonEmp.setScaledContents(True)
        self.label_ButtonEmp.setObjectName("label_ButtonEmp")
        self.label_ButtonEmp.mousePressEvent = self.event_screen3_2

        self.stackedWidget.addWidget(self.page_3)

        ## PAGE 4
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



        ## GIF BUTTONS
        self.label_ButtonScan1 = QtWidgets.QLabel(self.page_4)
        self.label_ButtonScan1.setGeometry(QtCore.QRect(590, 60, 391, 141))
        self.label_ButtonScan1.setText("")


        self.gif = QMovie('03-scan.gif')
        self.label_ButtonScan1.setMovie(self.gif)
        self.gif.start()
        self.label_ButtonScan1.setScaledContents(True)
        self.label_ButtonScan1.setObjectName("label_ButtonScan1")
        self.label_ButtonScan1.mousePressEvent = self.event_screen4_1

        self.label_ButtonScan2 = QtWidgets.QLabel(self.page_4)
        self.label_ButtonScan2.setGeometry(QtCore.QRect(610, 400, 391, 141))
        self.label_ButtonScan2.setText("")


        self.gif = QMovie('03-scan2.gif')
        self.label_ButtonScan2.setMovie(self.gif)
        self.gif.start()
        self.label_ButtonScan2.setScaledContents(True)
        self.label_ButtonScan2.setObjectName("label_ButtonScan2")
        self.label_ButtonScan2.mousePressEvent = self.event_screen4_2
        self.stackedWidget.addWidget(self.page_4)

        ## PAGE 5
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_bg5 = QtWidgets.QLabel(self.page_5)
        self.label_bg5.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label_bg5.setText("")
        self.label_bg5.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg5.setScaledContents(True)
        self.label_bg5.setObjectName("label_bg5")
        self.label_bg5.mousePressEvent = self.event_screen5
        self.stackedWidget.addWidget(self.page_5)





        ## PAGE 6
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_bg6 = QtWidgets.QLabel(self.page_6)
        self.label_bg6.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg6.setText("")
        self.label_bg6.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg6.setScaledContents(True)
        self.label_bg6.setObjectName("label_bg6")
        self.label_bg6.mousePressEvent = self.event_screen6


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
        self.stackedWidget.addWidget(self.page_6)




        ##PAGE 7

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
        self.label_bg7.mousePressEvent = self.event_screen7
        self.stackedWidget.addWidget(self.page_7)



        ## PAGE 8

        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_bg8 = QtWidgets.QLabel(self.page_8)
        self.label_bg8.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg8.setText("")
        self.label_bg8.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg8.setScaledContents(True)
        self.label_bg8.setObjectName("label_bg8")
        self.label_bg8.mousePressEvent = self.event_screen8

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
        self.stackedWidget.addWidget(self.page_8)

        ## PAGE 9

        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_bg9 = QtWidgets.QLabel(self.page_9)
        self.label_bg9.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label_bg9.setText("")
        self.label_bg9.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg9.setScaledContents(True)
        self.label_bg9.setObjectName("label_bg9")
        self.label_bg9.mousePressEvent = self.event_screen9

        self.message = QtWidgets.QLabel(self.page_9)
        self.message.setGeometry(QtCore.QRect(170, 180, 731, 251))
        self.message.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.message.setScaledContents(False)
        self.message.setObjectName("message")
        self.stackedWidget.addWidget(self.page_9)


        ## PAGE 10


        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_bg10 = QtWidgets.QLabel(self.page_10)
        self.label_bg10.setGeometry(QtCore.QRect(0, 0, 1021, 601))
        self.label_bg10.setText("")
        self.label_bg10.setPixmap(QtGui.QPixmap("1.gif"))
        self.label_bg10.setScaledContents(True)
        self.label_bg10.setObjectName("label_bg10")
        self.label_bg10.mousePressEvent = self.event_screen10

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
