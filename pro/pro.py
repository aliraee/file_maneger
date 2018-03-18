# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pro.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from zip_window import Ui_convert_to_zip_2
from view_image import Ui_view_image


class Ui_main_window(object):
    def open_zip_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_convert_to_zip_2()
        self.ui.setupUi(self.window)
        
        self.window.show()

    def open_image_page(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_view_image()
        self.ui.setupUi(self.window2)
        
        self.window2.show()
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowIcon(QtGui.QIcon('Bokehlicia-Captiva-File-manager.ico'))
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.zip = QtWidgets.QPushButton(self.centralwidget)
        self.zip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zip.setGeometry(QtCore.QRect(680, 70, 93, 28))
        self.zip.setObjectName("zip")

        self.zip.clicked.connect(self.open_zip_window)

        
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(680, 120, 93, 28))
        self.copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy.setObjectName("copy")
        self.cut = QtWidgets.QPushButton(self.centralwidget)
        self.cut.setGeometry(QtCore.QRect(680, 180, 93, 28))
        self.cut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cut.setObjectName("cut")
        self.view_image = QtWidgets.QPushButton(self.centralwidget)
        self.view_image.setGeometry(QtCore.QRect(680, 230, 93, 31))
        self.view_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view_image.setObjectName("view_image")

        self.view_image.clicked.connect(self.open_image_page)

        
        self.new_folder = QtWidgets.QPushButton(self.centralwidget)
        self.new_folder.setGeometry(QtCore.QRect(680, 280, 93, 28))
        self.new_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_folder.setObjectName("new_folder")
        self.reaname = QtWidgets.QPushButton(self.centralwidget)
        self.reaname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reaname.setGeometry(QtCore.QRect(680, 330, 93, 28))
        self.reaname.setObjectName("reaname")
        self.detail = QtWidgets.QPushButton(self.centralwidget)
        self.detail.setGeometry(QtCore.QRect(680, 380, 93, 28))
        self.detail.setObjectName("detail")
        self.detail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paste = QtWidgets.QPushButton(self.centralwidget)
        self.paste.setGeometry(QtCore.QRect(680, 430, 93, 28))
        self.paste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paste.setObjectName("paste")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 10, 451, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(630, 10, 141, 31))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_2.setObjectName("textEdit_2")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(main_window)
        self.cut.clicked.connect(self.textEdit.clear)
        self.copy.clicked.connect(self.textEdit.copy)
        self.paste.clicked.connect(self.textEdit_2.paste)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "File manager"))
        self.zip.setText(_translate("main_window", "Covert to Zip"))
        self.copy.setText(_translate("main_window", "Copy"))
        self.cut.setText(_translate("main_window", "Cut"))
        self.view_image.setText(_translate("main_window", "View img"))
        self.new_folder.setText(_translate("main_window", "New Folder"))
        self.reaname.setText(_translate("main_window", "Rename"))
        self.detail.setText(_translate("main_window", "Detail"))
        self.paste.setText(_translate("main_window", "Paste"))
        self.label.setText(_translate("main_window", "address :"))
        self.label_2.setText(_translate("main_window", "search :"))
        self.menuFile.setTitle(_translate("main_window", "File"))
        self.actionOpen.setText(_translate("main_window", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

