# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUiTest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimpleList(object):
    def setupUi(self, SimpleList):
        SimpleList.setObjectName("SimpleList")
        SimpleList.resize(1046, 608)
        self.centralwidget = QtWidgets.QWidget(SimpleList)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButtonBack = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonBack.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/resources/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonBack.setIcon(icon)
        self.toolButtonBack.setObjectName("toolButtonBack")
        self.horizontalLayout.addWidget(self.toolButtonBack)
        self.toolButtonUp = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/resources/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonUp.setIcon(icon1)
        self.toolButtonUp.setObjectName("toolButtonUp")
        self.horizontalLayout.addWidget(self.toolButtonUp)
        self.comboBoxPath = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPath.setEditable(True)
        self.comboBoxPath.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxPath.setObjectName("comboBoxPath")
        self.horizontalLayout.addWidget(self.comboBoxPath)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBoxPlaces = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPlaces.setObjectName("groupBoxPlaces")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxPlaces)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listViewPlaces = QtWidgets.QListView(self.groupBoxPlaces)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewPlaces.sizePolicy().hasHeightForWidth())
        self.listViewPlaces.setSizePolicy(sizePolicy)
        self.listViewPlaces.setObjectName("listViewPlaces")
        self.verticalLayout.addWidget(self.listViewPlaces)
        self.verticalLayout_3.addWidget(self.groupBoxPlaces)
        self.groupBoxConfig = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxConfig.sizePolicy().hasHeightForWidth())
        self.groupBoxConfig.setSizePolicy(sizePolicy)
        self.groupBoxConfig.setObjectName("groupBoxConfig")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxConfig)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxShowDirs = QtWidgets.QCheckBox(self.groupBoxConfig)
        self.checkBoxShowDirs.setObjectName("checkBoxShowDirs")
        self.verticalLayout_2.addWidget(self.checkBoxShowDirs)
        self.checkBoxShowHidden = QtWidgets.QCheckBox(self.groupBoxConfig)
        self.checkBoxShowHidden.setObjectName("checkBoxShowHidden")
        self.verticalLayout_2.addWidget(self.checkBoxShowHidden)
        self.checkBoxShowMediaInfo = QtWidgets.QCheckBox(self.groupBoxConfig)
        self.checkBoxShowMediaInfo.setObjectName("checkBoxShowMediaInfo")
        self.verticalLayout_2.addWidget(self.checkBoxShowMediaInfo)
        self.checkBoxMultiSelection = QtWidgets.QCheckBox(self.groupBoxConfig)
        self.checkBoxMultiSelection.setObjectName("checkBoxMultiSelection")
        self.verticalLayout_2.addWidget(self.checkBoxMultiSelection)
        self.checkBoxExtFsWatcher = QtWidgets.QCheckBox(self.groupBoxConfig)
        self.checkBoxExtFsWatcher.setObjectName("checkBoxExtFsWatcher")
        self.verticalLayout_2.addWidget(self.checkBoxExtFsWatcher)
        self.verticalLayout_3.addWidget(self.groupBoxConfig)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tableViewFM = QtWidgets.QTableView(self.centralwidget)
        self.tableViewFM.setObjectName("tableViewFM")
        self.horizontalLayout_2.addWidget(self.tableViewFM)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        SimpleList.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SimpleList)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        SimpleList.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SimpleList)
        self.statusbar.setObjectName("statusbar")
        SimpleList.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(SimpleList)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        SimpleList.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCopy = QtWidgets.QAction(SimpleList)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/resources/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(SimpleList)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/resources/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon3)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(SimpleList)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/resources/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon4)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(SimpleList)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/resources/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon5)
        self.actionDelete.setObjectName("actionDelete")
        self.actionMoveToTrash = QtWidgets.QAction(SimpleList)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/resources/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMoveToTrash.setIcon(icon6)
        self.actionMoveToTrash.setObjectName("actionMoveToTrash")
        self.actionGoUp = QtWidgets.QAction(SimpleList)
        self.actionGoUp.setIcon(icon1)
        self.actionGoUp.setObjectName("actionGoUp")
        self.actionGoBack = QtWidgets.QAction(SimpleList)
        self.actionGoBack.setIcon(icon)
        self.actionGoBack.setObjectName("actionGoBack")
        self.actionRename = QtWidgets.QAction(SimpleList)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resources/resources/edit-rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon7)
        self.actionRename.setObjectName("actionRename")
        self.actionNewFolder = QtWidgets.QAction(SimpleList)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resources/resources/folder-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFolder.setIcon(icon8)
        self.actionNewFolder.setObjectName("actionNewFolder")
        self.actionUndo = QtWidgets.QAction(SimpleList)
        self.actionUndo.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resources/resources/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionEmptyTrash = QtWidgets.QAction(SimpleList)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resources/resources/empty_trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmptyTrash.setIcon(icon10)
        self.actionEmptyTrash.setObjectName("actionEmptyTrash")
        self.actionRestoreFromTrash = QtWidgets.QAction(SimpleList)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/resources/resources/recyclebin_full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestoreFromTrash.setIcon(icon11)
        self.actionRestoreFromTrash.setObjectName("actionRestoreFromTrash")
        self.actionTerminnal = QtWidgets.QAction(SimpleList)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/resources/resources/xterm_48x48.xpm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerminnal.setIcon(icon12)
        self.actionTerminnal.setObjectName("actionTerminnal")
        self.actionOpen = QtWidgets.QAction(SimpleList)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCut_2 = QtWidgets.QAction(SimpleList)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionCopy_2 = QtWidgets.QAction(SimpleList)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionPaste_2 = QtWidgets.QAction(SimpleList)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionSave = QtWidgets.QAction(SimpleList)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCut_2)
        self.menuFile.addAction(self.actionCopy_2)
        self.menuFile.addAction(self.actionPaste_2)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionMoveToTrash)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addAction(self.actionNewFolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)

        self.retranslateUi(SimpleList)
        QtCore.QMetaObject.connectSlotsByName(SimpleList)

    def retranslateUi(self, SimpleList):
        _translate = QtCore.QCoreApplication.translate
        SimpleList.setWindowTitle(_translate("SimpleList", "MainWindow"))
        self.toolButtonBack.setText(_translate("SimpleList", "back"))
        self.toolButtonUp.setText(_translate("SimpleList", "Up"))
        self.groupBoxPlaces.setTitle(_translate("SimpleList", "Places"))
        self.groupBoxConfig.setTitle(_translate("SimpleList", "Configurations"))
        self.checkBoxShowDirs.setText(_translate("SimpleList", "show Directories"))
        self.checkBoxShowHidden.setText(_translate("SimpleList", "show Hidden Files"))
        self.checkBoxShowMediaInfo.setText(_translate("SimpleList", "show Multimedia"))
        self.checkBoxMultiSelection.setText(_translate("SimpleList", "activate Multiselection"))
        self.checkBoxExtFsWatcher.setText(_translate("SimpleList", "activate FS Watcher"))
        self.menuFile.setTitle(_translate("SimpleList", "file"))
        self.menuExit.setTitle(_translate("SimpleList", "Exit"))
        self.toolBar.setWindowTitle(_translate("SimpleList", "toolBar"))
        self.actionCopy.setText(_translate("SimpleList", "Copy"))
        self.actionCopy.setToolTip(_translate("SimpleList", "Copy Items into clipbpard"))
        self.actionCopy.setShortcut(_translate("SimpleList", "Ctrl+C"))
        self.actionCut.setText(_translate("SimpleList", "Cut"))
        self.actionCut.setToolTip(_translate("SimpleList", "Cut files into clipboard"))
        self.actionCut.setShortcut(_translate("SimpleList", "Ctrl+X"))
        self.actionPaste.setText(_translate("SimpleList", "Paste"))
        self.actionPaste.setToolTip(_translate("SimpleList", "paste clibpboard contents"))
        self.actionPaste.setShortcut(_translate("SimpleList", "Ctrl+V"))
        self.actionDelete.setText(_translate("SimpleList", "Remove"))
        self.actionDelete.setShortcut(_translate("SimpleList", "Shift+Del"))
        self.actionMoveToTrash.setText(_translate("SimpleList", "MoveToTrash"))
        self.actionMoveToTrash.setShortcut(_translate("SimpleList", "Del"))
        self.actionGoUp.setText(_translate("SimpleList", "Up"))
        self.actionGoUp.setToolTip(_translate("SimpleList", "Go parent folder"))
        self.actionGoUp.setShortcut(_translate("SimpleList", "Shift+U"))
        self.actionGoBack.setText(_translate("SimpleList", "Back"))
        self.actionGoBack.setShortcut(_translate("SimpleList", "Shift+B"))
        self.actionRename.setText(_translate("SimpleList", "Rename..."))
        self.actionNewFolder.setText(_translate("SimpleList", "NewFolder"))
        self.actionUndo.setText(_translate("SimpleList", "Undo"))
        self.actionEmptyTrash.setText(_translate("SimpleList", "EmptyTrash"))
        self.actionEmptyTrash.setToolTip(_translate("SimpleList", "EmptTrash"))
        self.actionRestoreFromTrash.setText(_translate("SimpleList", "RestoreFromTrash"))
        self.actionRestoreFromTrash.setToolTip(_translate("SimpleList", "restore From Trash"))
        self.actionTerminnal.setText(_translate("SimpleList", "Terminnal"))
        self.actionTerminnal.setToolTip(_translate("SimpleList", "open a Terminal"))
        self.actionOpen.setText(_translate("SimpleList", "open"))
        self.actionCut_2.setText(_translate("SimpleList", "cut"))
        self.actionCopy_2.setText(_translate("SimpleList", "copy"))
        self.actionPaste_2.setText(_translate("SimpleList", "paste"))
        self.actionSave.setText(_translate("SimpleList", "save"))

#import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimpleList = QtWidgets.QMainWindow()
    ui = Ui_SimpleList()
    ui.setupUi(SimpleList)
    SimpleList.show()
    sys.exit(app.exec_())

