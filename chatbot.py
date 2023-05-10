from tkinter import *
import chatgbt
root = Tk() 
root.attributes ("-fullscreen", True)

def send(event = None):
    txt.insert(END, "\nyou => "+ e.get())
    try:
        txt.insert(END, f"\nBot => {chatgbt.chatgpt(e.get())[2:]}")

    except:
        txt.insert(END, "\nBot => Response not found")

    e.delete(0,END)
#weather will be added on later 
frame = Frame(root)
txt = Text(frame)
txt.grid(row = 0, column = 0)
e = Entry(frame, width = 90)
sendButton = Button(frame, text = "send", command = send).grid(row = 1, column = 1)
e.grid(row = 1, column = 0)

frame.pack()

root.title("Walter")

root.bind('<Return>', send)

root.mainloop()