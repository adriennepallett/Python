from tkinter import *
import webbrowser

root = Tk()
root.title ("Social Media")

# Intro Statement
intxt = StringVar()
intro = Label(root, textvariable=intxt, padx = 25, pady = 25)
intxt.set("Check Out My Social Media")
intro.pack()

# Websites
Facebook = 1
urlf = "https://www.facebook.com/adriennepallett"
Twitter = 2
urlt = "https://twitter.com/AdriennePallett"
Pinterest = 3
urlp = "https://www.pinterest.com/adriennepallett"
Instagram = 4
urli = "https://www.instagram.com/adrienne.pallett/"

# Browser Functions
def openwebf():
    webbrowser.open(urlf,Facebook)
def openwebt():
    webbrowser.open(urlt,Twitter)
def openwebp():
    webbrowser.open(urlp,Pinterest)
def openwebi():
    webbrowser.open(urli,Instagram)

# Buttons
Btnf = Button(root, fg = "blue",text = "facebook",command=openwebf, padx = 5, pady = 5)
Btnf.pack()
Btnt = Button(root, fg = "cyan", text = "twitter",command=openwebt, padx = 5, pady = 5)
Btnt.pack()
Butp = Button(root, fg = "red", text = "pinterest", command=openwebp, padx = 5, pady = 5)
Butp.pack()
Buti = Button (root, fg = "magenta", text = "Instagram", command=openwebi, padx = 5, pady = 5)
Buti.pack()

root.mainloop()