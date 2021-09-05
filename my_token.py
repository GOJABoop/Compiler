class Token():
    def __init__(self, lineNumber, lexem, role):
        self.lineNumber = lineNumber
        self.lexem = lexem
        self.role = role

    def getLineNumber(self):
        return self.lineNumber

    def getLexem(self):
        return self.lexem
        
    def getRole(self):
        return self.role

    def toString(self):
        return str(self.lineNumber) + " " + self.lexem + " " + self.role