from tkinter import *
import subprocess

def addButton():
    subprocess.run(["python", "addGUI.py"])

def removeButton():
    subprocess.run(["python", "removeGUI.py"])

gui = Tk()

gui.title("To-Do List Organizer")
gui.geometry('360x240')

#introText = Label(gui, text = "Do you want to add or remove from the list?")
#introText.grid()

addButton = Button(gui, text = "Add", width = 24, command = addButton)
removeButton = Button(gui, text = "Remove", width = 24, command= removeButton )

addButton.grid(row=1,column=0)
removeButton.grid(row=1,column=1)

gui.mainloop()