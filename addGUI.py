from tkinter import *
import os.path


def setIndex():
    global index
    index = 1

setIndex()

if os.path.isfile("todolist.txt") is False:
    open("todolist.txt", 'x')

with open("todolist.txt", 'r') as f:
    global index
    for line in f:
        if line.strip() != "":
            index += 1

gui = Tk()

gui.title("Add Item To To-Do List")
gui.geometry('540x240')

text = Label(gui, text = "Put what item you want to add to the To-Do list here.")
text.grid()

entryItem = Entry(gui, width = 40)
entryItem.grid()

def addItemButton():
    global index
    text = entryItem.get()
    entryItem.delete(0,END)
    with open("todolist.txt", "a") as f:
        f.write(str(index) + ". " + text + "\n\n")
        index += 1

addButton = Button(gui, text="Add to list", command=addItemButton)
addButton.grid()

gui.mainloop()