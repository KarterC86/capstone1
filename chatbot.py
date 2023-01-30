from tkinter import *
root = Tk()
def send():
    #greetings
    semd = "you=>"+ e.get()
    txt.insert(END, "\n"+send)
    if(e.get()=="hello"):
        txt.instert(END, "\n"+"Bot => Hi")
    elif(e.get()=="how are you?"):
        txt.instert(END, "\n"+"Bot => Fine and you")
    elif(e.get()=="Fine"):
        txt.instert(END, "\n"+"Bot => That's great to hear")

    e.delete(0,END)
#weather will be added on later 


txt = Text(root)
txt.grid(row = 0, column = 0)
e = Entry(root, width = 100)
send = Button(root, text = "send")
e.grid (row = 1, column = 0 )
root.title("ChatBot")
root.mainloop()