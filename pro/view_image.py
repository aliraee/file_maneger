# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_image.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_image(object):
    def setupUi(self, view_image):
        view_image.setObjectName("view_image")
        view_image.resize(400, 300)
        self.open_image = QtWidgets.QPushButton(view_image)
        self.open_image.setGeometry(QtCore.QRect(180, 200, 93, 28))
        self.open_image.setObjectName("open_image")
        self.brows_img = QtWidgets.QPushButton(view_image)
        self.brows_img.setGeometry(QtCore.QRect(302, 130, 91, 28))
        self.brows_img.setObjectName("brows_img")
        self.textBrowser = QtWidgets.QTextBrowser(view_image)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(view_image)
        self.label.setGeometry(QtCore.QRect(30, 100, 141, 16))
        self.label.setObjectName("label")

        self.retranslateUi(view_image)
        QtCore.QMetaObject.connectSlotsByName(view_image)

    def retranslateUi(self, view_image):
        _translate = QtCore.QCoreApplication.translate
        view_image.setWindowTitle(_translate("view_image", "view image"))
        self.open_image.setText(_translate("view_image", "Open"))
        self.brows_img.setText(_translate("view_image", "Browse"))
        self.label.setText(_translate("view_image", "address of your photo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_image = QtWidgets.QWidget()
    ui = Ui_view_image()
    ui.setupUi(view_image)
    view_image.show()
    sys.exit(app.exec_())

