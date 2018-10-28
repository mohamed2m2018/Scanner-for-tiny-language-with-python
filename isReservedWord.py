reservedWords=["if","then","else","end","repeat","until","read","write"]

def isReservedWord(word):
    for reserved in reservedWords:
        if(word==reserved):
            return True
