from tkinter import *

mainscreen = Tk()
mainscreen.title ("Login Page")
#window.geometry("50x50")
mainscreen.attributes ("-fullscreen", True)

#trying to test full screen so that everything is on one page 
#window.attributes ("-fullscreen", True)
#window.attributes ("-fullscreen", False)


def loginScreen():
    #creating a label 
    Label(mainscreen, text = "Login Window", bg = "white", font=("Calibri", 13)).pack()
    Label(mainscreen, text="").pack()
    def openNewwindow():
        newWindow = Toplevel(mainscreen)
        newWindow.title ("sign in")
        newWindow.attributes ("-fullscreen", True)
        Label(newWindow, text = "please type in your username and password")

    #def validateLogin(username, password):
    #    print("username entered :", username.get())
    #    print("password entered :", password.get())


    #creating a login button 
    loginbutton = Button(mainscreen, text = "Login", command = openNewwindow,  height = "2" , width = "38")
    loginbutton.pack()
    Label(mainscreen, text = "").pack()


    #creat a register button
    Button(mainscreen, text = "Register", height = "2", width = "30").pack()
    



#btn = Button(mainscreen,
#text ="Click to open a new window",
#command = openNewwindow)


def registerScreen():
    pass

loginScreen()

mainscreen.mainloop() #start the GUI
