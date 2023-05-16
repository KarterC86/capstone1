from tkinter import *
import chatgbt
root = Tk() 

root.attributes ("-fullscreen", True)

currentWidgets = []
mainWidgets = []
SettingsWidgets = []


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


def SettingScreen ():
    global currentWidgets

    root.title ("Settings")
    root.attributes ("-fullscreen", True)
    deleteWidgets(currentWidgets)
    currentWidgets = SettingsWidgets
    packWidgets(currentWidgets)


def send(event = None):
    txt.insert(END, "\nyou => "+ e.get())
    try:
        txt.insert(END, f"\nBot => {chatgbt.chatgpt(e.get())[2:]}")

    except:
        txt.insert(END, "\nBot => Response not found")

    e.delete(0,END)


#weather will be added on later 
frame = Frame(root)

mainWidgets.append(frame)

txt = Text(frame)

txt.grid(row = 0, column = 0)
e = Entry(frame, width = 90)

sendButton = Button(frame, text = "send", command = send).grid(row = 1, column = 1)
exitButton = Button(frame, text = "exit", command = root.destroy).grid(row = 4, column = 4)
settingsButton = Button(frame, text = "Settings", command = SettingScreen).grid(row = 4, column = 6)
e.grid(row = 1, column = 0)

mainScreen()
root.title("Chatbot")
root.bind('<Return>', send)
root.mainloop()