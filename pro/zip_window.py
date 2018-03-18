# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zip_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_convert_to_zip_2(object):
    def setupUi(self, convert_to_zip_2):
        convert_to_zip_2.setObjectName("convert_to_zip_2")
        convert_to_zip_2.resize(400, 300)
        self.zip_text = QtWidgets.QTextEdit(convert_to_zip_2)
        self.zip_text.setGeometry(QtCore.QRect(40, 110, 241, 31))
        self.zip_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.zip_text.setObjectName("zip_text")
        self.label = QtWidgets.QLabel(convert_to_zip_2)
        self.label.setGeometry(QtCore.QRect(50, 70, 141, 16))
        self.label.setObjectName("label")
        self.convert_to_zip = QtWidgets.QPushButton(convert_to_zip_2)
        self.convert_to_zip.setGeometry(QtCore.QRect(170, 200, 93, 28))
        self.convert_to_zip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_to_zip.setObjectName("convert_to_zip")
        self.brows_zip = QtWidgets.QPushButton(convert_to_zip_2)
        self.brows_zip.setGeometry(QtCore.QRect(310, 110, 71, 31))
        self.brows_zip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.brows_zip.setObjectName("brows_zip")
        
        self.retranslateUi(convert_to_zip_2)
        QtCore.QMetaObject.connectSlotsByName(convert_to_zip_2)

      
    def retranslateUi(self, convert_to_zip_2):
        _translate = QtCore.QCoreApplication.translate
        convert_to_zip_2.setWindowTitle(_translate("convert_to_zip_2", "convert to zip"))
        self.label.setText(_translate("convert_to_zip_2", "Your folder address"))
        self.convert_to_zip.setText(_translate("convert_to_zip_2", "conver to zip"))
        self.brows_zip.setText(_translate("convert_to_zip_2", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    convert_to_zip_2 = QtWidgets.QWidget()
    ui = Ui_convert_to_zip_2()
    ui.setupUi(convert_to_zip_2)
    convert_to_zip_2.show()
    sys.exit(app.exec_())

