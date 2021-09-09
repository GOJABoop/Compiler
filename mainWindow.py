from PyQt6.QtWidgets import QMessageBox, QFileDialog, QMainWindow, QTableWidgetItem
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
        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setColumnWidth(1,80)
        self.tableWidget.setColumnWidth(2,200)

    def openFile(self):
        try:
            self.fileName = QFileDialog.getOpenFileName(self, 'Open file', 'C:', 'TXT files (*.txt)')
            self.plainTextEdit.clear()
            file = open(self.fileName[0], 'r')
            for line in file:
                self.plainTextEdit.appendPlainText("{}".format(line.strip()))
            file.close()
        except FileNotFoundError:
            self.messageBox()
        

    def saveFile(self):
        try:
            file = open(self.fileName[0],'w+')
            file.write(self.plainTextEdit.toPlainText())
            file.close()
        except IndexError:
            self.messageBox()
        except FileNotFoundError:
            self.messageBox()


    def compile(self):
        try:
            self.listWidgetError.clear()
            self.tableWidget.clearContents()
            tokens = Compiler.lexicalAnalysis(self.fileName[0])
            if(type(tokens) == str):
                self.listWidgetError.addItem(tokens)
            else:
                row = 0
                self.tableWidget.setRowCount(len(tokens))
                self.tableWidget.setColumnCount(3)
                for token in tokens:
                    self.tableWidget.setItem(row,0,QTableWidgetItem(str(token.getLineNumber())))
                    self.tableWidget.setItem(row,1,QTableWidgetItem(token.getLexem()))
                    self.tableWidget.setItem(row,2,QTableWidgetItem(token.getRole()))
                    row += 1
        except IndexError:
            self.messageBox()
        except FileNotFoundError:
            self.messageBox()


    def messageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Error: File not found")
        msg.setWindowTitle("Error")
        msg.exec()

