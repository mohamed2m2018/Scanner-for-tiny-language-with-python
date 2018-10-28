from isReservedWord import isReservedWord
from isIdentifier import isIdentifier
from isNumber import isNumber
from isSpecialSymbol import isSpecialSymbol
from isSpecialSymbol import checkSymbol
import re
import csv
import os.path
def parseCode(code):
    var=''
    if os.path.exists('Scanner_result.csv'):
        var='w'
    else:
        var='x'
    with open('Scanner_result.csv', mode=var) as Scanner_result:
        fieldnames = ['Token','Token type']
        writer = csv.DictWriter(Scanner_result, fieldnames=fieldnames)
        writer.writeheader()
        code = re.sub(r'\{[^{}]*\}', '', code)
        words = code.split()
        for word in words:
            if isReservedWord(word):
                writer.writerow({'Token': word, 'Token type': 'Reserved word'})

            elif isSpecialSymbol(word):
                wordLabel=checkSymbol(word)
                if word == "α":
                    word=":="
                if word=="μ":
                    word="*"
                writer.writerow({'Token': word, 'Token type': 'special symbol of type {}'.format(wordLabel)})

            elif isNumber (word):
                writer.writerow({'Token': word, 'Token type': 'Number'})
            else:
                writer.writerow({'Token': word, 'Token type': 'Identifier'})
