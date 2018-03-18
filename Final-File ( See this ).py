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

class window(QtGui.QMainWindow):
    
    def __init__(self):
        super(window, self).__init__()
        self.x = 640
        self.y = 480
        self.move(50, 50)
        self.setMinimumSize(self.x, self.y)
        self.setMaximumSize(self.x, self.y)
        self.setWindowTitle("Local File Manager")
        self.path = "\\"
        self.cutPath = None
        self.copyPath = None
        self.selected = None
        self.lst = os.listdir(self.path)
        self.select_count = 0
        self.init()

    
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
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
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

        width, height = 50, 25
        
        btn = QtGui.QPushButton("-->", self)
        btn.resize(width, height)
        btn.move(self.x - width, self.y - height)
        btn.clicked.connect(self.btn)

        self.textEdit = QtGui.QLineEdit(self)
        self.textEdit.resize(self.x - width*2, height - 2)
        self.textEdit.move(width, self.y - height + 2)
        self.textEdit.returnPressed.connect(self.btn)
        self.textEdit.setText(self.path)

        btn_back = QtGui.QPushButton("<--", self)
        btn_back.resize(width, height)
        btn_back.move(0, self.y - height)
        btn_back.clicked.connect(self.back)

        self.list = QtGui.QListView(self)
        self.list.resize(self.x, self.y - height*2)
        self.list.move(0, 20)
        self.list.setEditTriggers(QtGui.QListView.NoEditTriggers)
        self.list.doubleClicked.connect(self.doubleClick)
        self.list.clicked.connect(self.select)
        
        model = QtGui.QStandardItemModel(self.list)
        
        for item in self.lst:
            i = QtGui.QStandardItem(item)
            model.appendRow(i)
        
        self.list.setModel(model)
        self.list.show()
        self.show()

    def aboutus(self):
        os.startfile('Aboutus.txt')

    def help(self):
        os.startfile('Help.txt')

    def delete(self):
        if self.selected == None:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
            return None
        path = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.textEdit.text()+ self.lst[self.selected]
        else:
            path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        choice = QtGui.QMessageBox.question(self, "Delete ?", "Are you sure to Delete ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            shutil.rmtree(path)
            self.selected = None
            self.btn()
        else:
            return None
        
        
    def doubleClick(self):
        if self.path[len(self.path)-1] != "\\":
            self.path += "\\"+self.lst[self.selected]
        else:
            self.path += self.lst[self.selected]
        self.textEdit.setText(self.path)
        self.btn()
    
    def select(self):
        idx = self.list.selectionModel().selectedRows()
        for rec in idx:
            self.selected = rec.row() # return the index of selected item !

    def btn(self):
        self.path = self.textEdit.text()
        # print(self.path)
        if self.path == "":
            self.path = "\\"
        if os.path.exists(self.path):
            try:
                self.lst = os.listdir(self.path)
            except NotADirectoryError:
                os.startfile(self.path)
                self.back()
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Directory doesn't exists ! Please change it !")
        # Update the listView  
        model = QtGui.QStandardItemModel(self.list)
        for item in self.lst:
            i = QtGui.QStandardItem(item)
            model.appendRow(i)
        
        self.list.setModel(model)
        self.list.show()

    
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
            path = self.textEdit.text()+ new_name
            Cpath = self.textEdit.text() + self.lst[self.selected]
        else:
            path = self.textEdit.text()+"\\"+ new_name
            Cpath = self.textEdit.text() +"\\"+ self.lst[self.selected]
        path += os.path.splitext(Cpath)[1]
        os.rename(Cpath, path)
        self.selected = None
        self.btn()

    
    def back(self):
        self.selected = None
        if self.path.count('\\') == 1:
            self.path = '\\'
        else:
            Rpath = self.path[::-1]
            self.path= Rpath[Rpath.index('\\')+1:]
            self.path = self.path[::-1]
        if os.path.exists(self.path):
            self.textEdit.setText(self.path)
            self.btn()
    
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
            path = self.textEdit.text()+ new_name
        else:
            path = self.textEdit.text()+"\\"+ new_name
        os.makedirs(path)
        self.btn()
        
    
    def open(self):
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.textEdit.text()+ self.lst[self.selected]
            else:
                path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        os.startfile(path)
        pass

    
    def paste(self):# PermissionError on dirve that windows installed
        path = self.textEdit.text()
        if self.cutPath != None:
            try:
                shutil.move(self.cutPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(self, "Warning", "Can not access to %s" %self.textEdit.text())
            self.cutPath = None
            self.btn()
        elif self.copyPath != None:
            try:
                shutil.copy2(self.copyPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(self, "Warning", "Can not access to %s" %self.textEdit.text())
            self.copyPath = None
            self.btn()

    
    def copy(self): # Doesn't support folders
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.textEdit.text()+ self.lst[self.selected]
            else:
                path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.copyPath = path

    
    def cut(self): # Doesn't support folders
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.textEdit.text()+ self.lst[self.selected]
            else:
                path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.cutPath = path

    
    def exit(self):
        choice = QtGui.QMessageBox.question(self, "Exit ?", "Are you sure to exit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def main():
    app = QtGui.QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())


main()
