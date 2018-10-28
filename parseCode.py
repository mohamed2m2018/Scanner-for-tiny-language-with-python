from isReservedWord import isReservedWord
from isIdentifier import isIdentifier
from isNumber import isNumber
from isSpecialSymbol import isSpecialSymbol
from isSpecialSymbol import checkSymbol
import re
def parseCode(code):
    code=re.sub(r'\{[^{}]*\}', '', code)
    words=code.split()
    for word in words:
        if isReservedWord(word):
            print (word , "is reserved word")
        elif isSpecialSymbol(word):
            wordLabel=checkSymbol(word)
            if word == "α":
                word=":="
            if word=="μ":
                word="*"
            print (word, "is special symbol of the type",wordLabel)
        elif isNumber (word):
            print (word, "is a number")
        else:
            print(word ,"is identifier")
