from tkinter import *
from tkinter.ttk import *
import datetime
import os
from campbx import CampBX

class loginpopup:
    def __init__(self, master, cbxinstance):
        self.upfromme=master
        frame = Frame(master)
        frame.grid(column=0, row=0)
        
        self.usernamelab = Label(self.frame, text="Username:")
        self.usernamelab.grid(column=0, row=0)
        self.passwordlab = Label(self.frame, text="Password:")
        self.passwordlab.grid(column=0, row=1)
        
        self.username = StringVar()
        self.usernameentr = Entry(frame, textvariable=self.username)
        self.usernameentr.grid(column=1, row=0)
        self.username.set("")
        
        self.password = StringVar()
        self.passwordentr = Entry(frame, show="*", textvariable=self.password)
        self.passwordentr.grid(column=1, row=1)
        self.password.set("")
        
        self.login = Button(frame, text="login", command=logandexit)
        self.login.grid(column=0, row=2, columnspan=2)
        
    def loginandexit(self):
        print("not yet")