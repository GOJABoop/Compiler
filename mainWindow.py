from PyQt6.uic.load_ui import loadUi
from compiler import Compiler
from PyQt6.QtWidgets import QFileDialog, QHBoxLayout, QMainWindow, QTableWidgetItem, QTableWidget
from compiler import Compiler
from PyQt6 import uic
from my_token import Token

class MainWindow(QMainWindow):
    fileName = ''
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui", self)
        self.pushButtonOpen.clicked.connect(self.openFile)
        self.pushButtonSave.clicked.connect(self.saveFile)
        self.pushButtonCompile.clicked.connect(self.compile)
        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setColumnWidth(1,80)
        self.tableWidget.setColumnWidth(2,200)

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
        row = 0
        self.tableWidget.setRowCount(len(tokens))
        self.tableWidget.setColumnCount(3)
        for token in tokens:
            self.tableWidget.setItem(row,0,QTableWidgetItem(str(token.getLineNumber())))
            self.tableWidget.setItem(row,1,QTableWidgetItem(token.getLexem()))
            self.tableWidget.setItem(row,2,QTableWidgetItem(token.getRole()))
            row += 1
    

