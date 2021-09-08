from os import stat
import constants
from my_token import Token

tokens = []
multilineCommentsActivated = False
char = ''

def lexicalAnalyzer(fileName):
    countLines = 0
    tokens.clear()
    file = open(fileName)
    lines = file.readlines()
    for line in lines:
        countLines += 1
        try:
            findTokens(countLines, line)
        except Exception:
            return "At line " + str(countLines) + " error: " + char + " is not a valid id or operand"
    file.close()
    return tokens

def addNewToken(countLines, lexem, role):
    tokens.append(Token(countLines,lexem,role))

def isReservedWord(lexem):
    for word in constants.reservedWords:
        if (lexem == word):
            return True
    return False

def findTokens(countLines,line):
    i = 0
    state = 0
    lexem = ''
    global multilineCommentsActivated
    global char
    while(i < len(line)):
        char = line[i]
        if(multilineCommentsActivated == True and (i+1) <= len(line)):
            if(char == constants.MULTIPLICATION and line[i+1] == constants.DIVISION):
                multilineCommentsActivated = False
                i += 2
            else:
                i += 1
        else:
            if(state == 0):
                #MONOLEXEMS
                if(char == constants.COMMA):
                    addNewToken(countLines, constants.COMMA,constants.SEPARETOR)
                    i += 1
                elif(char == constants.OPENING_PARENTHESIS):
                    addNewToken(countLines, constants.OPENING_PARENTHESIS,constants.SEPARETOR)
                    i += 1
                elif(char == constants.LOCK_PARENTHESIS):
                    addNewToken(countLines, constants.LOCK_PARENTHESIS,constants.SEPARETOR)
                    i += 1
                elif(char == constants.OPENING_KEY):
                    addNewToken(countLines, constants.OPENING_KEY,constants.SEPARETOR)
                    i += 1
                elif(char == constants.LOCK_KEY):
                    addNewToken(countLines, constants.LOCK_KEY,constants.SEPARETOR)
                    i += 1
                elif(char == constants.SEMICOLON):
                    addNewToken(countLines, constants.SEMICOLON,constants.SEPARETOR)
                    i += 1
                elif(char == constants.AND):
                    addNewToken(countLines, constants.AND,constants.AND_OPERATION)
                    i += 1
                elif(char == constants.OR):
                    addNewToken(countLines,constants.OR,constants.OR_OPERATION)
                    i += 1
                #States for logical operations
                elif(char == constants.ASSIGNMENT):
                    state = 1
                    lexem += char
                    i += 1
                elif(char == constants.NEGATION):
                    state = 2
                    lexem += char
                    i += 1
                elif(char == constants.GREATER_THAN):
                    state = 3
                    lexem += char
                    i += 1
                elif(char == constants.LESS_THAN):
                    state = 4
                    lexem += char
                    i += 1
                #States for assignament operations
                elif(char == constants.ADDITION):
                    state = 5
                    lexem += char
                    i += 1
                elif(char == constants.SUBTRACTION):
                    state = 6
                    lexem += char
                    i += 1
                elif(char == constants.MULTIPLICATION):
                    state = 7
                    lexem += char
                    i += 1
                elif(char == constants.DIVISION):
                    state = 8
                    lexem += char
                    i += 1
                elif(char == constants.MODULE):
                    state = 9
                    lexem += char
                    i += 1
                elif(char == constants.UNDERSCORE or char.isalpha()):
                    state = 10
                    lexem += char
                    i += 1
                elif(char.isdigit()):
                    state = 11
                    lexem += char
                    i += 1
                elif(char == constants.SPACE or char == constants.TAB or char == constants.NEW_LINE):
                    i += 1
                else:
                    raise Exception()
            elif(state == 1):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"COMPARACION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"ASIGNACION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 2):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"DIFERENTE DE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"NEGACION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 3):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"MAYOR O IGUAL QUE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"MAYOR QUE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 4):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"MENOR O IGUAL QUE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"MENOR QUE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 5):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"ASIGNACION MAS SUMA")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"SIGNO SUMA")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 6):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"ASIGNACION MAS RESTA")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"SIGNO RESTA")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 7):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"ASIGNACION POR MULTIPLICACION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                elif(char == constants.MULTIPLICATION):
                    lexem += char
                    addNewToken(countLines,lexem,"SIGNO POTENCIA")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"SIGNO MULTIPLICACION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 8):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"ASIGNACION POR DIVISION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                elif(char == constants.DIVISION):
                    break 
                elif(char == constants.MULTIPLICATION):
                    multilineCommentsActivated = True
                    i += 1
                else:
                    addNewToken(countLines,lexem,"SIGNO DIVISION")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 9):
                if(char == constants.ASSIGNMENT):
                    lexem += char
                    addNewToken(countLines,lexem,"ASIGNACION POR MODULO")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
                    i += 1
                else:
                    addNewToken(countLines,lexem,"SIGNO MODULO")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 10):
                if(char == constants.UNDERSCORE or char.isalpha() or char.isdigit()):
                    lexem += char
                    i += 1
                else:
                    if(isReservedWord(lexem)):
                        addNewToken(countLines,lexem,"PALABRA RESERVADA")
                    else:
                        addNewToken(countLines,lexem,"IDENTIFICADOR")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 11):
                if(char.isdigit()):
                    lexem += char
                    i += 1
                elif(char == constants.DOT):
                    state = 12
                    lexem += char
                    i += 1
                else:
                    addNewToken(countLines,lexem,"NUMERO ENTERO")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER
            elif(state == 12):
                if(char.isdigit()):
                    lexem += char
                    i += 1
                else:
                    addNewToken(countLines,lexem,"NUMERO FLOTANTE")
                    state = 0
                    lexem = constants.EMPTY_CHARACTER