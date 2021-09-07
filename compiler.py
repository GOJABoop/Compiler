#The class Compiler calls to other components and modules
from lexical_analyzer import lexicalAnalyzer

class Compiler():
    def lexicalAnalysis(fileName):
        return lexicalAnalyzer(fileName)