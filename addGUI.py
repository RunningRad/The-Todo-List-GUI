from tkinter import *
import os.path

# Creates an index to show how many items are on the list.
def setIndex():
    global index
    index = 1

setIndex()

# Makes sure that a todolist.txt file already exists. If it doesn't, it creates the file.
if os.path.isfile("todolist.txt") is False:
    open("todolist.txt", 'x')

# Goes through the items in the ToDo list and increments the index for each item added.
with open("todolist.txt", 'r') as f:
    global index
    for line in f:
        if line.strip() != "":
            index += 1

# Creates GUI skeleton.
gui = Tk()

gui.title("Add Item To To-Do List")
gui.geometry('540x240')

text = Label(gui, text = "Put what item you want to add to the To-Do list here.")
text.grid()

entryItem = Entry(gui, width = 40)
entryItem.grid()

# Creates the add button functionality.
def addItemButton():
    global index

    # Takes the item and clears the text entry.
    text = entryItem.get()
    entryItem.delete(0,END)

    # Adds the text entry to the todo list.
    with open("todolist.txt", "a") as f:
        f.write(str(index) + ". " + text + "\n\n")
        index += 1

addButton = Button(gui, text="Add to list", command=addItemButton)
addButton.grid()

gui.mainloop()