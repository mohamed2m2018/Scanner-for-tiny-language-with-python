import tkinter as tk
from getCode import getCode

window = tk.Tk() #has the property of all stuff in tkinter

window.title ("Scanner App")

window.geometry("610x400")

#asking him for entering the code

label=tk.Label(text='Please enter code in tiny language')

label.grid(column=1,row=0,pady=5)

#textbox input field

input=tk.Text(master=window,height=10,width=80)

input.grid(column=1,row=1,padx=20,pady=20)

#button to submit code supplied by the command to be executed

button=tk.Button (master=window,text='Submit code',command=lambda :getCode(input))

button.grid(column=1,row=2,pady=7)

window.mainloop() # runs everything inside the window
