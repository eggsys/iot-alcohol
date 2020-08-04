from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")


        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 771, 471))
        self.label.setObjectName("label")
        self.retranslateUi(Form)

        self.gif = QMovie('03.gif')
        self.label.setScaledContents(True)
        self.label.setMovie(self.gif)
        self.gif.start()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
