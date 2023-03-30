from tkinter import *

mainscreen = Tk()
mainscreen.title ("Walter_ChatBot")

#window.geometry("50x50")
mainscreen.attributes ("-fullscreen", True)



responses = {'hello' : 'Hi', "Hello" : "Hi", '': 'sus', 'how are you' : 'Fine, and you', 'good': 'yay', 'what is your name?': "my name is Walter, I am your personal assistant with anything you may need.", "What is your favorite color?" : "I don't have a certain favorite, I like all colors.", "Can you help me?" : "Of course I can! I am an assistant to help with any of your issues. It is what I am made for.", "What were you made in?" : "My code was written in Python.", "Do you have a favorite animal?" : "I like all animals. Though the age-old question, are dogs or cats better?", "I like dogs" : "That is great to hear! They are very loyal to humans. They make very good fiends", "Dogs are better" : "That is interesting! They are very loyal pets to any human, very good friends!", "I like cats" : "I like to hear that. Cats like to go their own way.", "Cats are better" : "That is interesting! Fluffy little balls of chaotic energy!", "Thank you for the help" : "That is what I am here for"

}


def send(event = None):
    txt.insert(END, "\nyou => "+ e.get())
    try:
        txt.insert(END, f"\nBot => {responses[e.get()]}")

    except:
        txt.insert(END, "\nBot => Response not found")

    e.delete(0,END)

txt = Text(mainscreen)
txt.grid()
e = Entry(mainscreen, width = 40)
sendButton = Button(mainscreen, text = "Register",  height = "2" , width = "10")
e.grid (row = 1, column = 0)


mainscreen.title("Walter")

mainscreen.bind('<Return>', send)

mainscreen.mainloop()