from tkinter import *
from tkinter.ttk import *
import datetime
import os
from campbx import CampBX

class loginpopup:
    def __init__(self, master, cbxinstance):
        self.upfromme=master
        self.lframe = Frame(master)
        self.lframe.grid(column=0, row=0)
        
        self.usernamelab = Label(self.lframe, text="Username:")
        self.usernamelab.grid(column=0, row=0)
        self.passwordlab = Label(self.lframe, text="Password:")
        self.passwordlab.grid(column=0, row=1)
        
        self.username = StringVar()
        self.usernameentr = Entry(self.lframe, textvariable=self.username)
        self.usernameentr.grid(column=1, row=0)
        self.username.set(cbxinstance.username)
        
        self.password = StringVar()
        self.passwordentr = Entry(self.lframe, show="*", textvariable=self.password)
        self.passwordentr.grid(column=1, row=1)
        self.password.set(cbxinsance.password)
        
        self.login = Button(self.lframe, text="login", command=self.loginandexit)
        self.login.grid(column=0, row=2, columnspan=2)
        
    def loginandexit(self):
        cbxinstance.username = username
        cbxinstance.password = password
        print("not yet")