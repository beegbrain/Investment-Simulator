from tkinter import *
import  pandas as pd

#to create a window
root = Tk()

#root window is the parent window
fram = Frame(root)

#adding label to search box
Label(fram,text='Text to find:').pack(side=LEFT)

#adding of single line text box
edit = Entry(fram)

#positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

#setting focus
edit.focus_set()

#adding of search button
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

#text box in root window
text = Text(root)

#function to search string in text
def find():
    query = edit.get()
    returnData = pd.read_csv("https://ticker-2e1ica8b9.now.sh/keyword/"+query)

    print(returnData)

butt.config(command=find)

#mainloop function calls the endless loop of the window,
#so the window will wait for any
#user interaction till we close it
root.mainloop()

