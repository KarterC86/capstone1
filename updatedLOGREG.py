from tkinter import *

mainscreen = Tk()
mainscreen.title ("Login Page")
mainscreen.attributes ("-fullscreen", True)

currentWidgets = []
mainWidgets = []
registerWidgets = []
loginWidgets = []

def deleteWidgets(widgetList):
    for widget in widgetList:
        widget.forget()

def packWidgets(widgetList):
    for widget in widgetList:
        widget.pack()

def mainScreen():
    global currentWidgets

    deleteWidgets(currentWidgets)
    currentWidgets = mainWidgets
    packWidgets(currentWidgets)

def registerScreen():
    global currentWidgets

    mainscreen.title ("sign in")
    mainscreen.attributes ("-fullscreen", True)
    deleteWidgets(currentWidgets)
    currentWidgets = registerWidgets
    packWidgets(currentWidgets)

def loginScreen():
    global currentWidgets

    mainscreen.title ("Login")
    mainscreen.attributes ("-fullscreen", True)
    deleteWidgets(currentWidgets)
    currentWidgets = loginWidgets
    packWidgets(currentWidgets)



# main menu Widgets
mainWidgets.append(Label(mainscreen, text = "Login Window", bg = "white", font=("Calibri", 13)))
mainWidgets.append(Label(mainscreen, text=""))

#def validateLogin(username, password):
#    print("username entered :", username.get())
#    print("password entered :", password.get())


#creating a login button 
loginbutton = Button(mainscreen, text = "Login", command = loginScreen,  height = "2" , width = "38")
mainWidgets.append(loginbutton)
mainWidgets.append(Label(mainscreen, text = ""))

#creat a register button
registerbutton = Button(mainscreen, text = "Register", command = registerScreen,  height = "2" , width = "38")
mainWidgets.append(registerbutton)

# Register widgets
registerWidgets.append(Label(mainscreen, text = "please type in your username and password"))

inputBox = Frame(mainscreen)

userInput = Entry(inputBox)
userInput.grid(row = 0, column = 1)
Label(inputBox, text = 'Username:').grid(row = 0, column =0)

passInput = Entry(inputBox)
passInput.grid(row = 1, column = 1)
Label(inputBox, text = 'Password:').grid(row = 1, column =0)

registerWidgets.append(inputBox)

#creating an enter button 
enterbutton = Button(mainscreen, text = "enter", command = registerScreen, height = "2" , width = "38")
registerWidgets.append(enterbutton)

#creat a back button
backbutton = Button(mainscreen, text = "Back", command = mainScreen, height = "2" , width = "38")
registerWidgets.append(backbutton)

#adding a cloase window 
exit_button = Button(mainscreen, text="Exit", command = mainscreen.destroy)
exit_button.pack(pady=20)

# Login widgets
loginWidgets.append(Label(mainscreen, text = "please type in your username and password"))

inputBox = Frame(mainscreen)

userInput = Entry(inputBox)
userInput.grid(row = 0, column = 1)
Label(inputBox, text = 'Username:').grid(row = 0, column =0)

passInput = Entry(inputBox)
passInput.grid(row = 1, column = 1)
Label(inputBox, text = 'Password:').grid(row = 1, column =0)

loginWidgets.append(inputBox)

#creating an enter button 
enterbutton = Button(mainscreen, text = "enter", command = registerScreen, height = "2" , width = "38")
loginWidgets.append(enterbutton)

#creat a back button
backbutton = Button(mainscreen, text = "Back", command = mainScreen, height = "2" , width = "38")
loginWidgets.append(backbutton)

#btn = Button(mainscreen,
#text ="Click to open a new window",
#command = openNewwindow)


mainScreen()

mainscreen.mainloop() #start the GUI
