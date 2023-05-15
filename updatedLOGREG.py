from tkinter import *
from serverClass import Server

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

def loginact():
    userdata = Server('users.db')

    if loginUser.get() != '' and loginPass.get() != '':
        userdata.executeQuery(f'select Username, Password from accounts where Username like \'%{loginUser.get()}%\' and Password like \'%{loginPass.get()}%\'')
        
        if userdata.cursor.fetchall() != []:
            mainscreen.destroy()
            import chatbot

def registeract():
    userdata = Server('users.db')

    userdata.createTable('accounts', ['Username','Password', 'FirstName','LastName'], ['text','text','text','text'], ['unique','','',''])
    
    if userInput.get() != '' and passInput.get() != '' and lastname.get() !='' and firstname.get() !='':
        userdata.createRow('accounts',['Username','Password', 'FirstName','LastName'],[userInput.get(),passInput.get(), firstname.get(), lastname.get()])

    mainscreen.destroy()
    import chatbot

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

firstname = Entry(inputBox)
firstname.grid(row = 2, column = 1)
Label(inputBox, text = 'FirstName:').grid(row = 2, column =0)

lastname = Entry(inputBox)
lastname.grid(row = 3, column = 1)
Label(inputBox, text = 'LastName:').grid(row = 3, column =0)

registerWidgets.append(inputBox)

#creating an enter button 
enterbutton = Button(mainscreen, text = "enter", command = registeract, height = "2" , width = "38")
registerWidgets.append(enterbutton)

#creat a back button
backbutton = Button(mainscreen, text = "Back", command = mainScreen, height = "2" , width = "38")
registerWidgets.append(backbutton)


# Login widgets
loginWidgets.append(Label(mainscreen, text = "please type in your username and password"))

inputBox = Frame(mainscreen)

loginUser = Entry(inputBox)
loginUser.grid(row = 0, column = 1)
Label(inputBox, text = 'Username:').grid(row = 0, column =0)

loginPass = Entry(inputBox)
loginPass.grid(row = 1, column = 1)
Label(inputBox, text = 'Password:').grid(row = 1, column =0)

loginWidgets.append(inputBox)

#creating an enter button 
enterbutton = Button(mainscreen, text = "enter", command = loginact, height = "2" , width = "38")
loginWidgets.append(enterbutton)

#creat a back button
backbutton = Button(mainscreen, text = "Back", command = mainScreen, height = "2" , width = "38")
loginWidgets.append(backbutton)

#adding a cloase window 
exit_button = Button(mainscreen, text="Exit", command = mainscreen.destroy)
loginWidgets.append(exit_button)
registerWidgets.append(exit_button)
mainWidgets.append(exit_button)

#btn = Button(mainscreen,
#text ="Click to open a new window",
#command = openNewwindow)


mainScreen()

mainscreen.mainloop() #start the GUI