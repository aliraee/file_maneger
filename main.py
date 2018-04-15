"""
IUST - CE
March 2018
Please look at Help.txt and Aboutus.txt
BUGs :
    - PermissionError for writing on drive that windows installed !
    - Copy and Cut don't support folders
"""
import sys
import os # For managing directories
import shutil # For copy and cut and delete files
from PyQt4 import QtGui, QtCore # For UI
import sys
import socket
import string
import ctypes
myappid = 'iust.filemanager.anything.2' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

CHAT_MESS = ''
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.resize(500, 300)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.setFont(font)

        self.centralwidget = QtGui.QWidget(self)

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

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle("MainWindow")
        self.send.setText("Send")
        self.label.setText("message:")

    def sendIt(self):
        CHAT_MESS = self.lineEdit.text()
        if CHAT_MESS:
            self.lineEdit.setText('')
            self.textBrowser.append("[YOU]: " + CHAT_MESS)


class window_local(QtGui.QMainWindow):
    
    def __init__(self):
        """
        super(window_local, self).__init__()
        self.x = 640
        self.y = 480
        self.move(50, 50)
        self.setMinimumSize(self.x, self.y)
        self.setMaximumSize(self.x, self.y)
        self.setWindowTitle("Local File Manager")
        self.setWindowIcon(QtGui.QIcon('folder.ico'))
        self.path = ""
        self.cutPath = None
        self.copyPath = None
        self.selected = None
        self.connected = False
        self.searched = False
        self.drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        self.lst = self.drives
        self.select_count = 0
        self.init()"""
    def init(self):
        
        exitAction = QtGui.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the application")
        exitAction.triggered.connect(self.exit)

        openAction = QtGui.QAction("&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open the file")
        openAction.triggered.connect(self.open)

        newAction = QtGui.QAction("&New Folder", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Make new folder")
        newAction.triggered.connect(self.new)

        backAction = QtGui.QAction("&Back", self)
        backAction.setShortcut("Ctrl+Z")
        backAction.setStatusTip("Go to bacdirectory")
        backAction.triggered.connect(self.back)

        cutAction = QtGui.QAction("&Cut", self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.cut)

        copyAction = QtGui.QAction("&Copy", self)
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.copy)

        pasteAction = QtGui.QAction("&Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.paste)

        renameAction = QtGui.QAction("&Rename", self)
        renameAction.setShortcut("F2")
        renameAction.triggered.connect(self.rename)

        deleteAction = QtGui.QAction("&Delete", self)
        deleteAction.setShortcut("delete")
        deleteAction.triggered.connect(self.delete)

        helpAction = QtGui.QAction("&Help", self)
        helpAction.setShortcut("F1")
        helpAction.triggered.connect(self.help)

        usAction = QtGui.QAction("&About Us", self)
        usAction.setShortcut("F3")
        usAction.triggered.connect(self.aboutus)

        connectAction = QtGui.QAction("&Connect to remote device", self)
        connectAction.setShortcut("F4")
        connectAction.triggered.connect(self.connect_to_server)

        chatAction = QtGui.QAction("&Chat service", self)
        chatAction.setShortcut("F5")
        chatAction.triggered.connect(self.chat)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
        networkMenu = mainMenu.addMenu("&Network")
        moreMenu = mainMenu.addMenu("&More")
        
        fileMenu.addAction(openAction)
        fileMenu.addAction(newAction)
        fileMenu.addAction(backAction)
        fileMenu.addAction(exitAction)

        editMenu.addAction(cutAction)
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)
        editMenu.addAction(renameAction)
        editMenu.addAction(deleteAction)

        moreMenu.addAction(helpAction)
        moreMenu.addAction(usAction)

        networkMenu.addAction(connectAction)
        networkMenu.addAction(chatAction)

        width, height = 50, 25
        
        showDirs = QtGui.QPushButton("-->", self)
        showDirs.resize(width, height)
        showDirs.move(self.x - width, self.y - height)
        showDirs.clicked.connect(self.showDirs)

        self.EditDir = QtGui.QLineEdit(self)
        self.EditDir.resize(self.x - width * 2, height - 2)
        self.EditDir.move(width, self.y - height + 2)
        self.EditDir.returnPressed.connect(self.showDirs)
        self.EditDir.setText(self.path)

        self.EditSearch = QtGui.QLineEdit(self)
        self.EditSearch.resize(self.x - width, height)
        self.EditSearch.move(0, 21)
        self.EditSearch.returnPressed.connect(self.search)

        showDirs_search = QtGui.QPushButton("Search", self)
        showDirs_search.resize(width, height)
        showDirs_search.move(self.x - width, 20)
        showDirs_search.clicked.connect(self.search)

        showDirs_back = QtGui.QPushButton("<--", self)
        showDirs_back.resize(width, height)
        showDirs_back.move(0, self.y - height)
        #showDirs_back.setStyleSheet("QPushButton{background-image:url(M:\\MyProgramming\\workSpace\\Python\\file_manager_faze2\\icon_app.jpg);}")
        showDirs_back.clicked.connect(self.back)

        self.list = QtGui.QListView(self)
        self.list.resize(self.x, self.y - height*3 + 5)
        self.list.move(0, 47)
        self.list.setEditTriggers(QtGui.QListView.NoEditTriggers)
        self.list.doubleClicked.connect(self.doubleClick)
        self.list.clicked.connect(self.select)

        self.updateList(self.lst)
        self.show()
"""
    def updateList(self, list):
        model = QtGui.QStandardItemModel(self.list)
        for item in list:
            i = QtGui.QStandardItem(item)
            #i.setIcon(QtGui.QIcon('icon_app.jpg'))
            #i.setBackground(QtGui.QBrush(QtCore.Qt.lightGray))
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(12)
            font.setWeight(75)
            i.setFont(font)
            model.appendRow(i)
        self.list.setModel(model)
        self.list.show()
"""

    def chat(self):
        if not self.connected:
            QtGui.QMessageBox.warning(self, "Warning !", "Please connect to server first !")
        else:
            self.chatBox = Ui_MainWindow()
"""
    def search(self):
        forSearch = self.EditSearch.text()
        if not forSearch:
            self.path = "\\"
            self.EditDir.setText(self.path)
            self.showDirs()
            return None
        else:
            path = self.EditDir.text()
            self.lst = []
            if forSearch[0] == '.':
                print('test')
                print(forSearch)
                for root, dirs, filenames in os.walk(path):
                    for file in filenames:
                        if file.endswith(forSearch):
                            self.lst.append(os.path.join(root, file))
            else:
                for root, dirs, filenames in os.walk(path):
                    if forSearch in filenames:
                        self.lst.append(os.path.join(root, forSearch))
        if len(self.lst) != 0:
            self.searched = True
            self.updateList(self.lst)
        else:
            self.lst = os.listdir(self.path)
            QtGui.QMessageBox.warning(self, "File Not Found Erorr", "Please search full name of your file or just extension like(.txt)")
"""

    def aboutus(self):
        os.startfile('Aboutus.txt')

    def help(self):
        os.startfile('Help.txt')
"""
    def delete(self):
        if self.selected == None:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
            return None
        path = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.EditDir.text() + self.lst[self.selected]
        else:
            path = self.EditDir.text() + "\\" + self.lst[self.selected]
        choice = QtGui.QMessageBox.question(self, "Delete ?", "Are you sure to Delete ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            try:
                os.remove(path)
            except PermissionError:
                shutil.rmtree(path)
            self.selected = None
            self.showDirs()
        else:
            return None
            """
"""
    def doubleClick(self):
        if self.searched:
            self.EditDir.setText(self.lst[self.selected])
            self.showDirs()
            return None
        try:
            if self.path[len(self.path)-1] != "\\":
                self.path += "\\"+self.lst[self.selected]
            else:
                self.path += self.lst[self.selected]
        except:
            self.path = self.drives[self.selected]
        self.EditDir.setText(self.path)
        self.showDirs()
    
    def select(self):
        idx = self.list.selectionModel().selectedRows()
        for rec in idx:
            self.selected = rec.row() # return the index of selected item !
"""
"""
    def showDirs(self):
        self.path = self.EditDir.text()
        if os.path.exists(self.path):
            try:
                self.lst = os.listdir(self.path)
            except NotADirectoryError:
                os.startfile(self.path)
                self.back()
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Directory doesn't exists ! Please change it !")
        if self.path == "\\" or self.path == "":
            self.lst = self.drives
            self.path = ""
            self.EditDir.setText(self.path)
        # Update the listView
        self.updateList(self.lst)
""" 
"""
    def rename(self):
        if self.selected == None:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
            return None
        new_name, ok = QtGui.QInputDialog.getText(self, "Rename", "Please type the new name :")
        if not ok:
            return None
        if (ok and not new_name)or(new_name in self.lst):
            QtGui.QMessageBox.warning(self, "Warning", "New folder's name cann't be 'empty' or as 'same' as other file/folders !")
            return None
        path = self.path
        Cpath = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.EditDir.text() + new_name
            Cpath = self.EditDir.text() + self.lst[self.selected]
        else:
            path = self.EditDir.text() + "\\" + new_name
            Cpath = self.EditDir.text() + "\\" + self.lst[self.selected]
        path += os.path.splitext(Cpath)[1]
        os.rename(Cpath, path)
        self.selected = None
        self.showDirs()
"""
        
    """def back(self):
        if self.EditDir.text()!= "":
            self.selected = None
            if self.path.count('\\') == 1:
                if self.path[len(self.path)-1] == "\\":
                    self.path = "\\"
                else:
                    Rpath = self.path[::-1]
                    self.path = Rpath[Rpath.index('\\') + 1:]
                    self.path = self.path[::-1]+"\\"
            else:
                Rpath = self.path[::-1]
                self.path= Rpath[Rpath.index('\\')+1:]
                self.path = self.path[::-1]
            if os.path.exists(self.path):
                self.EditDir.setText(self.path)
                self.showDirs()
        else:
            return None"""
 """   
    def new(self):
        new_name, ok = QtGui.QInputDialog.getText(self, "New Folder", "Please type the name of new folder :")
        if not ok:
            return None
        if (ok and not new_name):
            new_name = "New folder" 
            if (new_name in self.lst):
                QtGui.QMessageBox.warning(self, "Warning", "New folder's name cann't be as same as other file/folders !")
                return None
        path = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.EditDir.text() + new_name
        else:
            path = self.EditDir.text() + "\\" + new_name
        os.makedirs(path)
        self.showDirs()"""
        
    """
    def open(self):
        path = self.path
        try:
            if self.selected != None:
                if self.path[len(self.path) - 1] == "\\":
                    path = self.EditDir.text() + self.lst[self.selected]
                else:
                    path = self.EditDir.text() + "\\" + self.lst[self.selected]
            else:
                QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        except IndexError:
            path = self.lst[self.selected]
        os.startfile(path)"""

    """    
    def paste(self):# PermissionError on dirve that windows installed
        path = self.EditDir.text()
        if self.cutPath != None:
            try:
                shutil.move(self.cutPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(self, "Warning", "Can not access to %s" % self.EditDir.text())
            self.cutPath = None
            self.showDirs()
        elif self.copyPath != None:
            try:
                shutil.copy2(self.copyPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(self, "Warning", "Can not access to %s" % self.EditDir.text())
            self.copyPath = None
            self.showDirs()
"""
    """
    def copy(self): # Doesn't support folders
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.EditDir.text() + self.lst[self.selected]
            else:
                path = self.EditDir.text() + "\\" + self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.copyPath = path

    
    def cut(self): # Doesn't support folders
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.EditDir.text() + self.lst[self.selected]
            else:
                path = self.EditDir.text() + "\\" + self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.cutPath = path
    """
    """
    def exit(self):
        choice = QtGui.QMessageBox.question(self, "Exit ?", "Are you sure to exit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
             pass   """

APP = QtGui.QApplication(sys.argv)
#QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
START =  window_local()
HOST = ''
PORT = ''
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER = 1024
sys.exit(APP.exec_())
