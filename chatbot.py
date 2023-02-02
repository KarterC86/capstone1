from tkinter import *
root = Tk() 

responses = {'hello' : 'Hi', '': 'sus', 'how are you' : 'Fine, and you', 'good': 'yay',


}
def send():
    txt.insert(END, "\nyou => "+ e.get())

    if(e.get()=="Play Game"):
        txt.insert(END, "\n"+"Bot => ")
    # elif(e.get()=="how are you?"):
    #     txt.insert(END, "\n"+"Bot => Fine and you")
    # elif(e.get()=="Fine"):
    #     txt.insert(END, "\n"+"Bot => That's great to hear")
    try:
        txt.insert(END, f"\nBot => {responses[e.get()]}")

    except:
        txt.insert(END, "\nBot => Response not found")

    e.delete(0,END)
#weather will be added on later 


txt = Text(root)
txt.grid(row = 0, column = 0)
e = Entry(root, width = 90)
send = Button(root, text = "send", command = send).grid(row = 1, column = 1)
e.grid (row = 1, column = 0 )
root.title("ChatBot")
root.mainloop()