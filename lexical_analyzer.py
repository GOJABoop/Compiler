import constants
from my_token import Token

tokens = []

def lexicalAnalyzer(fileName):
    countLines = 0
    tokens.clear()
    file = open(fileName)
    lines = file.readlines()
    for line in lines:
        countLines += 1
        findTokens(countLines, line)
    file.close()
    return tokens

def findTokens(countLines,line):
    i = 0
    lexem = ''
    while(i < len(line)):
        #MONOLEXEMS
        if(line[i] == constants.COMMA):
            addNewToken(countLines, constants.COMMA,constants.SEPARETOR)
            i += 1
        elif(line[i] == constants.OPENING_PARENTHESIS):
            addNewToken(countLines, constants.OPENING_PARENTHESIS,constants.SEPARETOR)
            i += 1
        elif(line[i] == constants.LOCK_PARENTHESIS):
            addNewToken(countLines, constants.LOCK_PARENTHESIS,constants.SEPARETOR)
            i += 1
        elif(line[i] == constants.OPENING_KEY):
            addNewToken(countLines, constants.OPENING_KEY,constants.SEPARETOR)
            i += 1
        elif(line[i] == constants.LOCK_KEY):
            addNewToken(countLines, constants.LOCK_KEY,constants.SEPARETOR)
            i += 1
        elif(line[i] == constants.SEMICOLON):
            addNewToken(countLines, constants.SEMICOLON,constants.SEPARETOR)
            i += 1
        else:
            i += 1

def addNewToken(countLines, lexem, role):
    tokens.append(Token(countLines,lexem,role))