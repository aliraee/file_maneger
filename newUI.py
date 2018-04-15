# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# UI by: Ali Ayati, Ali Raee

# import modules
from PyQt4 import QtCore, QtGui     # For designing the UI
import icons  # For loading icons
import os                           # For browsing directories
import shutil                       # For Copy, Cut and Delete

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def __init__(self):
        self.path = "/home"
        self.cutPath = None
        self.copyPath = None
        self.selected = None
        self.connected = False
        self.searched = False
        self.lst = os.listdir(self.path)
        self.select_count = 0

    def setupUi(self, MainWindow):
        # Generate the UI
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(719, 450)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.move(50, 50)
        MainWindow.setWindowTitle("Local File Manager")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/folder.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.showDirs)
        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_back = QtGui.QPushButton(self.centralwidget)
        self.btn_back.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/back.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.btn_back.clicked.connect(self.back)
        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_go = QtGui.QPushButton(self.centralwidget)
        self.btn_go.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/go.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_go.setIcon(icon1)
        self.btn_go.setObjectName(_fromUtf8("btn_go"))
        self.btn_go.clicked.connect(self.showDirs)
        self.horizontalLayout.addWidget(self.btn_go)

        self.btn_new = QtGui.QPushButton(self.centralwidget)
        self.btn_new.setText(_fromUtf8(""))
        self.btn_new.clicked.connect(self.new)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new.setIcon(icon2)
        self.btn_new.setObjectName(_fromUtf8("btn_new"))
        self.horizontalLayout.addWidget(self.btn_new)

        self.btn_home = QtGui.QPushButton(self.centralwidget)
        self.btn_home.setText(_fromUtf8(""))
        self.btn_home.clicked.connect(self.home)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/home.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon3)
        self.btn_home.setObjectName(_fromUtf8("btn_home"))
        self.horizontalLayout.addWidget(self.btn_home)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView.setEditTriggers(QtGui.QListView.NoEditTriggers)
        self.listView.doubleClicked.connect(self.doubleClick)
        self.listView.clicked.connect(self.select)
        self.verticalLayout_2.addWidget(self.listView)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdite = QtGui.QMenu(self.menubar)
        self.menuEdite.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuEdite.setObjectName(_fromUtf8("menuEdite"))
        self.menuNetwork = QtGui.QMenu(self.menubar)
        self.menuNetwork.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuNetwork.setObjectName(_fromUtf8("menuNetwork"))
        self.menuMore = QtGui.QMenu(self.menubar)
        self.menuMore.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuMore.setObjectName(_fromUtf8("menuMore"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(self.open)

        self.actionNew_Folder = QtGui.QAction(MainWindow)
        self.actionNew_Folder.setObjectName(_fromUtf8("actionNew_Folder"))
        self.actionNew_Folder.triggered.connect(self.new)

        self.actionBack = QtGui.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionBack.triggered.connect(self.back)

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.exit)

        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCut.triggered.connect(self.cut)

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCopy.triggered.connect(self.copy)

        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionPaste.triggered.connect(self.paste)

        self.actionRename = QtGui.QAction(MainWindow)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        self.actionRename.triggered.connect(self.rename)

        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionDelete.triggered.connect(self.delete)

        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionChat = QtGui.QAction(MainWindow)
        self.actionChat.setObjectName(_fromUtf8("actionChat"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionHelp.triggered.connect(self.help)

        self.actionAbout_Us = QtGui.QAction(MainWindow)
        self.actionAbout_Us.setObjectName(_fromUtf8("actionAbout_Us"))
        self.actionAbout_Us.triggered.connect(self.about)

        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionSearch.triggered.connect(self.search)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionNew_Folder)
        self.menuFile.addAction(self.actionBack)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdite.addAction(self.actionCut)
        self.menuEdite.addAction(self.actionCopy)
        self.menuEdite.addAction(self.actionPaste)
        self.menuEdite.addAction(self.actionRename)
        self.menuEdite.addAction(self.actionDelete)
        self.menuNetwork.addAction(self.actionConnect)
        self.menuNetwork.addAction(self.actionChat)
        self.menuMore.addAction(self.actionHelp)
        self.menuMore.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdite.menuAction())
        self.menubar.addAction(self.menuNetwork.menuAction())
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Look in : ", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdite.setTitle(_translate("MainWindow", "Edit", None))
        self.menuNetwork.setTitle(_translate("MainWindow", "Network", None))
        self.menuMore.setTitle(_translate("MainWindow", "More", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionNew_Folder.setText(_translate("MainWindow", "New Folder", None))
        self.actionNew_Folder.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionBack.setText(_translate("MainWindow", "Back", None))
        self.actionBack.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionRename.setText(_translate("MainWindow", "Rename", None))
        self.actionRename.setShortcut(_translate("MainWindow", "F2", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionConnect.setShortcut(_translate("MainWindow", "F3", None))
        self.actionChat.setText(_translate("MainWindow", "Chat", None))
        self.actionChat.setShortcut(_translate("MainWindow", "F4", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1", None))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us", None))
        self.actionAbout_Us.setShortcut(_translate("MainWindow", "F5", None))
        self.actionSearch.setText(_translate("MainWindow", "Search", None))
        self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.updateList(self.lst)

    def about(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("About Us")
        msg.setInformativeText("Project File Manager")
        msg.setWindowTitle("About Us")
        msg.setDetailedText("""IUST - CE
Developers:
    - Seyyed Ali Ayati
    - Ali Raee
    - Mir Hossein
    - AmirReza Zand""")
        #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(msgbtn)
        retval = msg.exec_()

    def help(self):
        os.system('xdg-open '+"'"+'Help.txt'+"'")

    def copy(self):
        self.path = self.lineEdit.text()
        path = ''
        if self.selected != None:
            if self.path[len(self.path) - 1] == "/":
                path = self.lineEdit.text() + self.lst[self.selected]
            else:
                path = self.lineEdit.text() + "/" + self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(MainWindow, "Warning", "Please select a file or folder !")
        self.copyPath = path


    def cut(self):
        self.path = self.lineEdit.text()
        path = ''
        if self.selected != None:
            if self.path[len(self.path) - 1] == "/":
                path = self.lineEdit.text() + self.lst[self.selected]
            else:
                path = self.lineEdit.text() + "/" + self.lst[self.selected]
        else:
            QtGui.QMessageBox.warning(MainWindow, "Warning", "Please select a file or folder !")
        self.cutPath = path

    def paste(self):
        path = self.lineEdit.text()
        if self.cutPath != None:
            try:
                shutil.move(self.cutPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(MainWindow, "Warning", "Can not access to %s" % self.lineEdit.text())
            self.cutPath = None
            self.showDirs()
        elif self.copyPath != None:
            try:
                shutil.copy2(self.copyPath, path)
            except PermissionError:
                QtGui.QMessageBox.warning(MainWindow, "Warning", "Can not access to %s" % self.lineEdit.text())
            self.copyPath = None
            self.showDirs()

    def rename(self):
        if self.selected == None:
            QtGui.QMessageBox.warning(MainWindow, "Warning", "Please select a file or folder !")
            return None
        new_name, ok = QtGui.QInputDialog.getText(MainWindow, "Rename", "Please type the new name :")
        if not ok:
            return None
        if (ok and not new_name) or (new_name in self.lst):
            QtGui.QMessageBox.warning(MainWindow, "Warning", "New folder's name cann't be 'empty' or as 'same' as other file/folders !")
            return None
        path = ''
        Cpath = ''
        if self.path[len(self.path) - 1] == "/":
            path = self.lineEdit.text() + new_name
            Cpath = self.lineEdit.text() + self.lst[self.selected]
        else:
            path = self.lineEdit.text() + "/" + new_name
            Cpath = self.lineEdit.text() + "/" + self.lst[self.selected]
        path += os.path.splitext(Cpath)[1]
        os.rename(Cpath, path)
        self.selected = None
        self.showDirs()

    def delete(self):
        if self.selected == None:
            QtGui.QMessageBox.warning(MainWindow, "Warning", "Please select a file or folder !")
            return None
        path = ''
        if self.path[len(self.path) - 1] == "/":
            path = self.lineEdit.text() + self.lst[self.selected]
        else:
            path = self.lineEdit.text() + "/" + self.lst[self.selected]
        choice = QtGui.QMessageBox.question(MainWindow, "Delete ?", "Are you sure to Delete ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            try:
                os.remove(path)
            except:
                shutil.rmtree(path)
            self.selected = None
            self.showDirs()
        else:
            return None

    def updateList(self, List):
        model = QtGui.QStandardItemModel(self.listView)
        for item in List:
            i = QtGui.QStandardItem(item)
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(12)
            font.setWeight(75)
            icon = QtGui.QIcon()
            extension = os.path.splitext(item)[1]
            if extension == '':
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/folder2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            elif extension == '.mp3' or extension=='wav':
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/music.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            elif extension == '.mp4' or extension == '.avi' or extension == '.wmv' or extension == '.mpg':
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/video.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            elif extension == '.txt':
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/text.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            elif extension == '.jpg' or extension == '.ico' or extension == '.png':
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pic.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else :
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/none.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            i.setFont(font)
            i.setIcon(icon)
            model.appendRow(i)
        self.listView.setModel(model)
        self.listView.show()

    def doubleClick(self):
        self.path = self.lineEdit.text()
        if self.path == '':
            self.path = "/home"
        if self.searched:
            self.searched = False
            self.path = self.lst[self.selected]
            self.lineEdit.setText(self.path)
            self.showDirs()
            return None
        try:
            self.lst = os.listdir(self.path)
        except NotADirectoryError as e:
            self.open()
        
        if self.path[len(self.path)-1] != "/":
            self.path += "/"+self.lst[self.selected]
        else:
            self.path += self.lst[self.selected]
        self.lineEdit.setText(self.path)
        try:
            self.lst = os.listdir(self.path)
        except NotADirectoryError:
            os.system("xdg-open "+"'"+self.path+"'")
            self.back()
            return None
        self.updateList(self.lst)
        pass

    def select(self):
        idx = self.listView.selectionModel().selectedRows()
        for rec in idx:
            self.selected = rec.row() # return the index of selected item !
        pass

    def showDirs(self):
        self.path = self.lineEdit.text()
        if os.path.exists(self.path):
            try:
                self.lst = os.listdir(self.path)
            except NotADirectoryError:
                os.system("xdg-open "+"'"+self.path+"'")
                self.back()
        else:
            QtGui.QMessageBox.warning(MainWindow, "Warning", "Directory doesn't exists ! Please change it !")
        if self.path == "/" or self.path == "":
            self.lst = self.drives
            self.path = ""
            self.lineEdit.setText(self.path)
        # Update the listView
        self.updateList(self.lst)
        pass

    def back(self):
        self.selected = None
        current_dir = self.lineEdit.text()
        try:
            current_dir = current_dir[::-1]
            index = current_dir.index('/')
            new_dir = current_dir[index+1:]
            new_dir = new_dir[::-1]
            self.path = new_dir
        except ValueError:
            self.path = "/home"
        if self.path == "":
            self.path = '/home'
        self.lst = os.listdir(self.path)
        self.updateList(self.lst)
        self.lineEdit.setText(self.path)

    def new(self):
        new_name, ok = QtGui.QInputDialog.getText(MainWindow, "New Folder", "Please type the name of new folder :")
        if not ok:
            return None
        if (ok and not new_name):
            new_name = "New folder" 
            if (new_name in self.lst):
                QtGui.QMessageBox.warning(self, "Warning", "New folder's name cann't be as same as other file/folders !")
                return None
        self.path = self.lineEdit.text()
        path = self.path
        if self.path[len(self.path) - 1] == "/":
            path = self.lineEdit.text() + new_name
        else:
            path = self.lineEdit.text() + "/" + new_name
        os.makedirs(path)
        self.showDirs()
    
    def home(self):
        self.path = "/home"
        self.lineEdit.setText(self.path)
        self.showDirs()

    def open(self):
        self.path = self.lineEdit.text()
        path = self.path
        try:
            self.lst = os.listdir(path)
        except NotADirectoryError:
            os.system("xdg-open "+"'"+path+"'")
            return None
        try:
            if self.selected != None:
                if self.path[len(self.path) - 1] == "/":
                    path = self.lineEdit.text() + self.lst[self.selected]
                else:
                    path = self.lineEdit.text() + "/" + self.lst[self.selected]
            else:
                QtGui.QMessageBox.warning(MainWindow, "Warning", "Please select a file or folder !")
        except IndexError:
            path = self.lst[self.selected]
        os.system("xdg-open "+"'"+path+"'")
        #self.back()

    def search(self):
        searched, ok = QtGui.QInputDialog.getText(MainWindow, "New Folder", "Please type the name of new folder :")
        if not ok:
            return None
        forSearch = searched
        if not forSearch:
            self.path = "/"
            self.lineEdit.setText(self.path)
            self.showDirs()
            return None
        else:
            path = self.lineEdit.text()
            self.lst = []
            if forSearch[0] == '.':
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
            QtGui.QMessageBox.warning(MainWindow, "File Not Found Erorr", "Please search full name of your file or just extension like(.txt)")

    def exit(self):
        choice = QtGui.QMessageBox.question(MainWindow, "Exit ?", "Are you sure to exit ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
