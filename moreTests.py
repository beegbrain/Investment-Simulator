from tkinter import *
import  pandas as pd
import csv
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
aList=["hi"]
def find():
    global aList
    query = edit.get()
    returnData = pd.read_csv("https://ticker-2e1ica8b9.now.sh/keyword/"+query)
    returnData= list(returnData)
    aList = []
    for i in range(0,len(returnData),2):
        returnData[i]=returnData[i].split('"')
        aList.append(returnData[i][-2])
    dropDown = OptionMenu(root,default,*aList)

butt.config(command=find)
default = StringVar(root)
default.set(aList[0])
dropDown = OptionMenu(root,default,*aList)
dropDown.pack()
#mainloop function calls the endless loop of the window,
#so the window will wait for any
#user interaction till we close it
root.mainloop()
