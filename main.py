import threading
import tkinter.messagebox
from datetime import datetime

import pyttsx3

#pip install tk-tools
from TODOclass import Item
tasks = []
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button

# create a tkinker based ui





def alarmhandler():
    for alarm in tasks:
        print("{}:{}".format(alarm.name,alarm.time))

        if(alarm.time == datetime.now().strftime("%I:%M %p")):
            s = pyttsx3.init()
            s.say("{}".format("GO AND  {} ".format(alarm.name)))
            s.runAndWait()
            tasks.remove(alarm)


    root.after(1000, alarmhandler)




root = tkinter.Tk()
class SimpleDialog(tkinter.Frame):

    def __init__(self):
        super().__init__()
        # self allow the variable to be used anywhere in the class
        self.output1 = ""
        self.output2 = ""
        self.output3 = ""
        self.output4 = ""
        self.initUI()

    def initUI(self):

        self.master.title("Simple Dialog")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="TaskName", width=9)
        lbl1.pack(side=LEFT, padx=10, pady=10)

        self.entry1 = Entry(frame1, textvariable=self.output1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="TaskDesc", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=10)

        self.entry2 = Entry(frame2,textvariable=self.output2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="Soundtoplay", width=9)
        lbl3.pack(side=LEFT, padx=5, pady=10)


        self.entry3 = Entry(frame3, textvariable=self.output3)
        self.entry3.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        lbl4 = Label(frame4, text="Time", width=9)
        lbl4.pack(side=LEFT, padx=5, pady=10)
        self.entry4 = Entry(frame4, textvariable=self.output4)
        self.entry4.pack(fill=X, padx=5, expand=True)







        frame4 = Frame(self)
        frame4.pack(fill=X)

        # Command tells the form what to do when the button is clicked
        btn = Button(frame4, text="Submit", command=self.onSubmit)
        btn.pack(padx=5, pady=10)

    def onSubmit(self):


        if(self.entry1.get() != "") and self.entry2.get() != "" and self.entry3.get() != ""  and self.entry4.get() != "" and self.is_valid_datetime(self.entry4.get()):
            self.output1 = self.entry1.get() # PERFECT NAME
            self.output2 = self.entry2.get() #PERFECT DESCRIPTION
            self.output3 = self.entry4.get() # TIME
            self.output4 = self.entry3.get() # SOUND
            tasks.append(Item(self.output1,self.output2,self.output3,self.output4))


            self.destroy()
        else:
            tkinter.messagebox.showwarning("Please fill up the form")

    def is_valid_datetime(self, datetime_str):
        try:
            # Attempt to parse the input string into a datetime object
            datetime.strptime(datetime_str,  "%I:%M %p")
            return True
        except ValueError:
            return False





def message():
    tkinter.messagebox.showinfo("Hello")
username = 'username' # change this to ur needs

# while  1:
#     currenttime = datetime.now().strftime("%I:%M %p")
#     if(datetime.now().strftime("%I")) <="9":
#         print("YES LESS THAN NINE")
#         break
#
#     if(currenttime == "09:18 PM"):
#         print("YES")
#         break

threading.Thread(target=alarmhandler, daemon=True).start()
root.title("TODO")
root.minsize(200, 200)  # width, height
xcentre = (root.winfo_screenwidth() - 530) / 2
ycentre = (root.winfo_screenmmheight() - 200) / 2
root.geometry("{}x{}+{}+{}".format(600,530,int(xcentre),int(ycentre+100)))
# Create Label in our window
text = tkinter.Label(root, text="TODO list")
text.pack()
text2 = tkinter.Label(root, text="WELCOME {}!".format(username))
text2.pack()
# plus button which will require the user to enter their task.
plusbutton = tkinter.Button(root,text="+",command=SimpleDialog)
plusbutton.pack()
root.mainloop()

