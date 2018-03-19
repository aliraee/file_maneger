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
from PyQt5 import QtGui, QtCore  , QtWidgets# For UI
from zipfile import *

class window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(window, self).__init__()
        self.x = 640
        self.y = 480
        self.move(50, 50)
        self.setMinimumSize(self.x, self.y)
        self.setMaximumSize(self.x, self.y)
        self.setWindowTitle("Local File Manager")
        self.setWindowIcon(QtGui.QIcon("Bokehlicia-Captiva-File-manager.ico"))

        
        self.path = "\\"
        self.cutPath = None
        self.copyPath = None
        self.selected = None
        self.lst = os.listdir(self.path)
        self.select_count = 0
        self.init()

    
    def init(self):
        
        exitAction = QtWidgets.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the application")
        exitAction.triggered.connect(self.exit)

        openAction = QtWidgets.QAction("&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open the file")
        openAction.triggered.connect(self.open)

        saveAction = QtWidgets.QAction("&save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("save the file")
        saveAction.triggered.connect(self.file_save)



        newAction = QtWidgets.QAction("&New Folder", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Make new folder")
        newAction.triggered.connect(self.new)


        zipAction = QtWidgets.QAction("&Zip File", self)
        zipAction.setShortcut("Ctrl+F")
        zipAction.setStatusTip("COnvert to zip")
        zipAction.triggered.connect(self.zip)


        openEditor = QtWidgets.QAction ("&Editor" , self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)

        backAction = QtWidgets.QAction("&Back", self)
        backAction.setShortcut("Ctrl+Z")
        backAction.setStatusTip("Go to bacdirectory")
        backAction.triggered.connect(self.file_save)

        cutAction = QtWidgets.QAction("&Cut", self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.cut)

        copyAction = QtWidgets.QAction("&Copy", self)
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.copy)

        pasteAction = QtWidgets.QAction("&Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.paste)

        renameAction = QtWidgets.QAction("&Rename", self)
        renameAction.setShortcut("F2")
        renameAction.triggered.connect(self.rename)

        deleteAction = QtWidgets.QAction("&Delete", self)
        deleteAction.setShortcut("delete")
        deleteAction.triggered.connect(self.delete)

        helpAction = QtWidgets.QAction("&Help", self)
        helpAction.setShortcut("F1")
        helpAction.triggered.connect(self.help)

        usAction = QtWidgets.QAction("&About Us", self)
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
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openEditor)
        fileMenu.addAction(zipAction)
        fileMenu.addAction(exitAction)

        editMenu.addAction(cutAction)
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)
        editMenu.addAction(zipAction)
        editMenu.addAction(deleteAction)

        moreMenu.addAction(helpAction)
        moreMenu.addAction(usAction)

        width, height = 50, 25
        
        btn = QtWidgets.QPushButton("-->", self)
        btn.resize(width, height)
        btn.move(self.x - width, self.y - height)
        btn.clicked.connect(self.btn)

        self.textEdit = QtWidgets.QLineEdit(self)
        self.textEdit.resize(self.x - width*2, height - 2)
        self.textEdit.move(width, self.y - height + 2)
        self.textEdit.returnPressed.connect(self.btn)
        self.textEdit.setText(self.path)

        btn_back = QtWidgets.QPushButton("<--", self)
        btn_back.resize(width, height)
        btn_back.move(0, self.y - height)
        btn_back.clicked.connect(self.back)

        self.list = QtWidgets.QListView(self)
        self.list.resize(self.x, self.y - height*2)
        self.list.move(0, 20)
        self.list.setEditTriggers(QtWidgets.QListView.NoEditTriggers)
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
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
            return None
        path = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.textEdit.text()+ self.lst[self.selected]
        else:
            path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        choice = QtWidgets.QMessageBox.question(self, "Delete ?", "Are you sure to Delete ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
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


    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self,"save File")
        

        if name[0] != '':
            file = open(name[0] , 'w')
            text = self.textEdit.toPlainText()

            file.write(text)
            file.close()
        else:
            pass


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
            QtWidgets.QMessageBox.warning(self, "Warning", "Directory doesn't exists ! Please change it !")
        # Update the listView  
        model = QtGui.QStandardItemModel(self.list)
        for item in self.lst:
            i = QtGui.QStandardItem(item)
            model.appendRow(i)
        
        self.list.setModel(model)
        self.list.show()



    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)



    
    def rename(self):
        if self.selected == None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
            return None
        new_name, ok = QtWidgets.QInputDialog.getText(self, "Rename", "Please type the new name :")
        if not ok:
            return None
        if (ok and not new_name)or(new_name in self.lst):
            QtWidgets.QMessageBox.warning(self, "Warning", "New folder's name cann't be 'empty' or as 'same' as other file/folders !")
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
        new_name, ok = QtWidgets.QInputDialog.getText(self, "New Folder", "Please type the name of new folder :")
        if not ok:
            return None
        if (ok and not new_name):
            new_name = "New folder" 
            if (new_name in self.lst):
                QtWidgets.QMessageBox.warning(self, "Warning", "New folder's name cann't be as same as other file/folders !")
                return None
        path = self.path
        if self.path[len(self.path) - 1] == "\\":
            path = self.textEdit.text()+ new_name
        else:
            path = self.textEdit.text()+"\\"+ new_name
        os.makedirs(path)
        self.btn()
        
    
    def open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self , "open File")
        #print(QtWidgets.QFileDialog.FileType())
        print(name)

        if name[0] != '':
            file = open (name[0] , 'r')
            print(file)
            self.editor()

            with file :
                text = file.read()
                self.textEdit.setText(text)
        else:
            pass

        
        
        '''
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.textEdit.text()+ self.lst[self.selected]
            else:
                path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        os.startfile(path)
        pass
        '''
    
    def paste(self):# PermissionError on dirve that windows installed
        path = self.textEdit.text()
        if self.cutPath != None:
            try:
                shutil.move(self.cutPath, path)
            except PermissionError:
                QtWidgets.QMessageBox.warning(self, "Warning", "Can not access to %s" %self.textEdit.text())
            self.cutPath = None
            self.btn()
        elif self.copyPath != None:
            try:
                shutil.copy2(self.copyPath, path)
            except PermissionError:
                QtWidgets.QMessageBox.warning(self, "Warning", "Can not access to %s" %self.textEdit.text())
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
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.copyPath = path


    def zip(self):
        text , ok = QtWidgets.QInputDialog.getText(None , 'Zip Save' ,"Enter your zip file's name :")
        if ok == True :
            
            file_name = QtWidgets.QFileDialog.getOpenFileName(self , "Witch you want to convert to ZIP")

            if file_name[0] != '':
                
                zip_file = ZipFile(text + '.zip' , "w")
                zip_file.write(file_name[0])
                zip_file.close()
                
            else:
                pass
        else:
            pass

    
    def cut(self): # Doesn't support folders
        path = self.path
        if self.selected != None:
            if self.path[len(self.path) - 1] == "\\":
                path = self.textEdit.text()+ self.lst[self.selected]
            else:
                path = self.textEdit.text()+"\\"+ self.lst[self.selected]
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a file or folder !")
        self.cutPath = path

    
    def exit(self):
        choice = QtWidgets.QMessageBox.question(self, "Exit ?", "Are you sure to exit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())


main()
