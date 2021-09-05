from compiler import Compiler
from PyQt6.QtWidgets import QFileDialog, QMainWindow
from compiler import Compiler
from PyQt6 import uic

class MainWindow(QMainWindow):
    fileName = ''
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui", self)
        self.pushButtonOpen.clicked.connect(self.openFile)
        self.pushButtonSave.clicked.connect(self.saveFile)
        self.pushButtonCompile.clicked.connect(self.compile)

    def openFile(self):
        self.fileName = QFileDialog.getOpenFileName(self, 'Open file', 'C:', 'TXT files (*.txt)')
        self.plainTextEdit.clear()
        file = open(self.fileName[0], 'r')
        for line in file:
            self.plainTextEdit.appendPlainText("{}".format(line.strip()))
        file.close()

    def saveFile(self):
        file = open(self.fileName[0],'w+')
        file.write(self.plainTextEdit.toPlainText())
        file.close()

    def compile(self):
        tokens = Compiler.lexicalAnalysis(self.fileName[0])
        self.plainTextEdit.clear()
        for token in tokens:
           self.plainTextEdit.appendPlainText("{}".format(token.toString()))