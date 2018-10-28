from tkinter import *
from tkinter import ttk
from getCode import getCode

window= Tk() #has the property of all stuff in tkinter

window.style=ttk.Style()

window.style.theme_use("vista")

window.title ("Scanner App")

window.wm_state('zoomed')

#asking him for entering the code

label=ttk.Label(text='Please enter code in tiny language',font='Helvetica 14 bold')

label.grid(column=1,row=0,pady=10)

#scroll bar

scrollbar = Scrollbar(window)
scrollbar.grid(column=2,row=1,sticky=N+S+W)


#textbox input field

input=Text(master=window,width=50,bg="#FFF8DC",insertbackground="green",
           fg="green",font='Helvetica 14 bold',yscrollcommand=scrollbar.set)

scrollbar.configure(command=input.yview)


input.grid(column=1,row=1,padx=(20,0),pady=20)


#button to submit code supplied by the command to be executed

button=ttk.Button (master=window,text='Submit code',command=lambda :getCode(input))
button.grid(column=1,row=2,pady=7)



window.mainloop()
