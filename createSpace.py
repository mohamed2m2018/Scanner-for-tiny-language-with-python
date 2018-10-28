from isSpecialSymbol import isSpecialSymbol
import re
def concatenate_list_data(list):
	    result= ''
	    for element in list:
	        result += str(element)
	    return result

def createSpace(code):
    spaceCodeList=[]
    code=code.replace(":=","α")
    code=code.replace("*","μ")
    for index,character in enumerate(code):
        if isSpecialSymbol(character):
            spaceCodeList.clear()
            splits=re.split('({})'.format(character),code)
            for split in splits:
                spaceCodeList.append(split)
                if(split!=" "):
                    spaceCodeList.append(" ")
                code=str(concatenate_list_data(spaceCodeList))

    s=str(concatenate_list_data(spaceCodeList))
    print(s)
    return s
