import sys
from PyQt5 import QtGui , QtCore , QtWidgets

class Window (QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self ).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("File Manager")
        self.setWindowIcon(QtGui.QIcon("Bokehlicia-Captiva-File-manager.ico"))

        
        extractionAction = QtWidgets.QAction("&Quit!!",self)
        extractionAction.setShortcut("Ctrl+Q")
        extractionAction.setStatusTip("Leave the app")
        extractionAction.triggered.connect(self.close_application)

        openEditor = QtWidgets.QAction ("&Editor" , self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)

        openFile = QtWidgets.QAction ("&Open File" , self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_open)

        saveFile = QtWidgets.QAction ("&Save File" , self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save File")
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("&File")

        fileMenu.addAction(extractionAction)
        
        fileMenu.addAction(openFile)
        
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)
        
        self.home()


    def home(self):
        
        btn = QtWidgets.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,65)
        
        extractionAction =  QtWidgets.QAction(QtGui.QIcon("python-logo@2x.png"),'Falee the scene',self)
        extractionAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractionAction)
        

        fontChoice = QtWidgets.QAction("Font " , self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar.addAction(fontChoice)

        
        Openning = QtWidgets.QAction("Open",self)
        Openning.triggered.connect(self.file_open)
        self.toolBar.addAction(Openning)

        #checkBox = QtWidgets.QCheckBox("Enlarge Window" , self)
        #checkBox.move(300,25)
        #checkBox.stateChanged.connect(self.enlarge_window)
        

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtWidgets.QPushButton("Extract",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)


        self.styleChoice = QtWidgets.QLabel("Best Group",self)

        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("Amirreza_zand")
        comboBox.addItem("Ali_raee")
        comboBox.addItem("ali_ayati")
        comboBox.addItem("mir_hossein")
        


        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        #cal = QtWidgets.QCalendarWidget(self)
        #cal.move(500,200)
        #cal.resize(200,200)
        
        self.show()
    

    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self , "open File")
        file = open(name , "r")
        self.editor()

        with file :
            text = file.read()
            self.textEdit.setText(text)
        




    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFile(self , 'save File')

    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def font_choice(self ):
        font , valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
    

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    

    def download(self):
        self.completed = 0

        while self.completed <100 :
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def enlarge_window (self , state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)


    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self,'Extract!' , "Do you want to Quit" , QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes :
            print ("Extracting naaooooowwwww!!")
            sys.exit()

        else:
            pass


app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

        
        
        
        
        

