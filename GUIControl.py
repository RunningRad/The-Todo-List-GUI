from tkinter import *
import subprocess

# Runs the addGUI.py page.
def addButton():
    subprocess.run(["python", "addGUI.py"])

# Runs the removeGUI.py page.
def removeButton():
    subprocess.run(["python", "removeGUI.py"])

# Initializes the GUI
gui = Tk()

# Basic code that gives the GUI it's structure.
gui.title("To-Do List Organizer")
gui.geometry('360x240')

#introText = Label(gui, text = "Do you want to add or remove from the list?")
#introText.grid()

# Creates the buttons for the GUI
addButton = Button(gui, text = "Add", width = 24, command = addButton)
removeButton = Button(gui, text = "Remove", width = 24, command= removeButton )

addButton.grid(row=1,column=0)
removeButton.grid(row=1,column=1)

# Runs the GUI
gui.mainloop()