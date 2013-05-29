from tkinter import *
from tkinter.ttk import *
import datetime
import os
from campbx import CampBX

class loginpopup:
    def __init__(self, master, cbxinstance, whobebig):
        self.upfromme=whobebig
        self.metkroot=master
        self.lframe = Frame(master)
        self.lframe.grid(column=0, row=0)
        
        self.usernamelab = Label(self.lframe, text="Username:")
        self.usernamelab.grid(column=0, row=0)
        self.passwordlab = Label(self.lframe, text="Password:")
        self.passwordlab.grid(column=0, row=1)
        
        
        self.usernameentr = Entry(self.lframe)
        self.usernameentr.grid(column=1, row=0)
        
        self.passwordentr = Entry(self.lframe, show="*")
        self.passwordentr.grid(column=1, row=1)
        
        self.login = Button(self.lframe, text="login", command=self.loginandexit)
        self.login.grid(column=0, row=2, columnspan=2)
        
    def loginandexit(self):
        creds = { "username" : str(self.usernameentr.get()) , "password" : str(self.passwordentr.get()) }
        print(creds)
        self.upfromme.connection.setcred(creds)
        self.metkroot.destroy()
        return
        