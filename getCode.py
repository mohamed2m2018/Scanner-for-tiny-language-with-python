import tkinter as tk
from parseCode import parseCode
from createSpace import createSpace
def getCode(input):
    label=tk.Label(text='\n \n Congratulations our dear user :D \n'
                        'The result is added successfully to '
                        'csv file \n in the same directory of this exe \n \n',
                   font='Helvetica 14 bold',
                   fg='#FFFFFF',
                   bg='#EA5E3D',
                   padx=100
                   )
    label.grid(column=3,row=1)
    code=str(input.get("1.0","end-1c"))
    code=createSpace(code)
    parseCode(code)

