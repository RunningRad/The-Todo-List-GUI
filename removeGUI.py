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
def populateListbox():
    with open("todolist.txt", 'r') as f:
        for line in f:
            if line.strip() != "":
                listOfTasks.insert(listOfTasks.size()+1, line)

populateListbox()

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
    
    # Removes the item of the given index.
    with open("todolist.txt", "r") as f:
        item = f.readlines()
        listIndex = index * 2
    
    del item[listIndex]
    del item[listIndex]

    newItems = []
    counter = 1

    # Creates a new list with the correct index and item contents.
    for thing in item:
        if thing != '\n':
           itemContents = thing.split(".", 1)
           newItems.append(str(counter) + "." + itemContents[1])
           counter += 1
        else:
            newItems.append(thing)       

    # Deletes current file contents.
    open("todolist.txt", 'w').close()

    # Writes new file contents to the file, and repopulates the listbox
    with open("todolist.txt", 'w') as f:
        f.writelines(newItems)

    listOfTasks.delete(0,END)
    populateListbox()        

# Puts the remove item on the GUI
removeItemButton = Button(gui, text="Remove from list", command=removeItemButton)
removeItemButton.grid(column=1,row=1)

# Creates GUI
gui.mainloop()