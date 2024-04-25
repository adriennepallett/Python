from tkinter import *
from tkinter import messagebox

root = Tk()
root.title ("So You Wanna Do Math?")
root.pack()

intro = Label(root, text="...Let's Get To It!")
intro.pack

# First Number Entered By User
firstnumber = Label(root,text="First Number")
a = Entry(root)
a = StringVar (root,a)

# Second Number Entered By User
lbl2 = Label(root,text="Second Number")
lbl2.pack
b = Entry(root, width="20")
b.pack
b = StringVar (root, b)

def addtwo (a,b):
    return a + b
def subtwo (a,b):
    return a - b
def multtwo (a,b):
    return a * b
def divtwo (a,b):
    return a / b

# Operator
operate1 = Radiobutton (root, text = "Add", value ="1")
operate1.pack

operate2 = Radiobutton (root, text = "Subtract", value = "2")
operate2.pack

operate3 = Radiobutton (root, text = "Multiply", value = "3")
operate3.pack

operate4 = Radiobutton (root, text = "Divide", value = "4")
operate4.pack

# Run Result Button
def clicked():
    messagebox.showinfo("Your answer is:", "RESULT")
    
btncal = Button(root,text="Let's Go!", command=clicked)
btncal.pack



root.mainloop()