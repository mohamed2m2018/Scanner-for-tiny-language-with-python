import tkinter as tk
from parseCode import parseCode
from createSpace import createSpace
def getCode(input):
    label=tk.Label(text='your code has been added successfully')
    label.grid(column=1,row=3)
    code=str(input.get("1.0","end-1c"))
    code=createSpace(code)
    parseCode(code)
