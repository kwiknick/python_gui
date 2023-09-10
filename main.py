from cgitb import text
from faulthandler import disable
from tkinter import *

root = Tk()

entryWidget = Entry(root, width=50)
entryWidget.pack()
entryWidget.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + entryWidget.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()

