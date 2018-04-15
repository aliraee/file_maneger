from file_maneger.chatBox import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
#from file_maneger.server_chat import *
#from file_maneger.client_chat import *
from file_maneger.server_chat import *
class merge(Ui_MainWindow):
    def __init__(self,to):
        super(merge,self).__init__()
        self.messageList=[]
        self.txt='hello'
        self.server=server(to)
    def sendMSG(self,to):
        if to=='server':
            self.server.send('server :'+self.lineEdit.text())
        else:
            self.server.send('client :' + self.lineEdit.text())
    def recive(self,to):
        if to=='server':
            msg='client :'+self.server.recive()
            self.messageList+=[msg]
        else:
            msg = 'server :' + self.server.recive()
            self.messageList += [msg]

    def event(self):
        self.send.clicked.connect(self.showText)
        self.clear.clicked.connect(self.Clear)
        self.edit.clicked.connect(self.Edit)
        self.attach.clicked.connect(self.Attach)
        #self.sendMSG(self.to)
    def Attach(self):
        pass #file manager ro baz kone
    def Edit(self):
        #self.lineEdit.setText(self.string)
        self.Clear()
        #self.messageList=[]
        try:
            for i in range(0,len(self.messageList)-1):
                self.textBrowser.append('message from user 1:'+self.messageList[i])
        except IndexError:
            pass
        temp=self.messageList[-1]
        del (self.messageList[-1])
        self.lineEdit.setText(temp)


    def Clear(self):
        self.textBrowser.clear()
    def showText(self):
        if self.lineEdit.text()!='':
            self.recive('server')
            self.sendMSG('server')
            self.txt=self.lineEdit.text()
            self.textBrowser.append('message from user 1:'+ self.lineEdit.text())
            self.messageList+=[self.lineEdit.text()]
            self.lineEdit.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = merge('server')
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.event()
    sys.exit(app.exec_())
