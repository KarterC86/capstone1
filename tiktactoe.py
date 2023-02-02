from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Walter's Tic-Tac-Toe")
#root.geometry('1200x710')

#button clicked function 
def b_click(b):
    pass


#to build our button
b1 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
b2 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
b3 = Button(root,text = " ", font = ('Droid Sans Mono', 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))

b4 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
b5 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
b6 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))

b7 = Button(root,text = " ", font = ("Droid Sans Mono, 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
b8 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8))
b9 = Button(root,text = " ", font = ("Droid Sans Mono", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9))
 #griding our buttons to the screen
 
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)


b4.grid(row = 0, column = 0)
b5.grid(row = 0, column = 1)
b6.grid(row = 0, column = 2)

b7.grid(row = 0, column = 0)
b8.grid(row = 0, column = 1)
b9.grid(row = 0, column = 2)

root.mainloop()
