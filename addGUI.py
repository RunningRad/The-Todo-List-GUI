from tkinter import *

gui = Tk()

gui.title("Add Item To To-Do List")
gui.geometry('540x240')

text = Label(gui, text = "Put what item you want to add to the To-Do list here.")
text.grid()

entryItem = Entry(gui, width = 40)
entryItem.grid()

def addItemButton():
    print(entryItem.get())

addButton = Button(gui, text="Add to list", command=addItemButton)
addButton.grid()

gui.mainloop()