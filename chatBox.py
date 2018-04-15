# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatBox.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(700, 568)
        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        MainWindow.setFont(font)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        
        self.send = QtGui.QPushButton(self.centralwidget)
        self.send.clicked.connect(self.sendIt)
        self.gridLayout.addWidget(self.send, 1, 3, 1, 1)
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.returnPressed.connect(self.sendIt)
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 33))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.send.setText("Send")
        self.label.setText("message:")

    def sendIt(self):
        for_send = self.lineEdit.text()
        if for_send:
            self.lineEdit.setText('')
            self.textBrowser.append("[YOU]: "+for_send)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

