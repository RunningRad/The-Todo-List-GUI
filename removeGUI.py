from tkinter import *
import os.path

# Creates GUI skeleton.
gui = Tk()

gui.title("Remove Item From To-Do List")
gui.geometry('540x360')

# Makes sure that a todolist.txt file already exists. If it doesn't, it creates the file.
if os.path.isfile("todolist.txt") is False:
    open("todolist.txt", 'x')

# Creates listbox that displays tasks
listOfTasks = Listbox(gui, height = 10, width = 15, bg = "grey", activestyle = 'dotbox', font = "Helvetica", fg = "yellow")
listOfTasks.grid()

# Puts items from the file onto the listbox.
with open("todolist.txt", 'r') as f:
    for line in f:
        if line.split() != "":
            listOfTasks.insert(listOfTasks.size()+1, line)

# Creates the entry box to remove a task.
removeIndex = Entry(gui, width = 40)
removeIndex.grid(column = 0, row = 1)

# Remove Item Button Command
def removeItemButton():
    # Gets the index from the entry
    index = removeIndex.get()
    removeIndex.delete(0,END)

    # Verifies that the entry is an integer
    if index.isdigit() is False:
        print("Not a valid index, must be an integer.")
        return
    
    # Reduces the index that was input to be used in the listbox
    index = int(index) - 1

    # Checks to make sure the index is in range.
    if (index < 0):
        print("Not a valid index, entered value is less than one.")
        return
    elif (index > listOfTasks.size()-1):
        print("Not a valid index, there is not item with the index " + str(index + 1))
        return
    else:
        print(index)

# Puts the remove item on the GUI
removeItemButton = Button(gui, text="Add to list", command=removeItemButton)
removeItemButton.grid(column=1,row=1)

# Creates GUI
gui.mainloop()