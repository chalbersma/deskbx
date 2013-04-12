from tkinter import *
import datetime
import os
from campbx import CampBX

class GUI:
    def __init__(self, master):

        self.upfromme=master

        frame = Frame(master)
        frame.grid(column=0, row=0, columnspan=4)

        #Menu
        self.menu = Menu(master)
        master.config(menu = self.menu)

        #Description Label
        self.pricetickerdesc=Label(frame,text="Price")
        self.pricetickerdesc.grid(row=0)
        self.biddesc=Label(frame,text="Bid")
        self.biddesc.grid(row=0,column=1)
        self.biddesc=Label(frame,text="Ask")
        self.biddesc.grid(row=0,column=2)
        
        #Current Price Label
        self.priceticker=Label(frame,text="Last...")
        self.priceticker.grid(row=1)
        self.bidticker=Label(frame,text="Bid...")
        self.bidticker.grid(row=1,column=1)
        self.askticker=Label(frame,text="Ask...")
        self.askticker.grid(row=1,column=2)
        
        self.priceupdate=Button(frame, text="Update", command=self.updateprice())
        self.priceupdate.grid(row=2)
        
        self.note=Label(frame,text="Prices pulled from Campbx")
        self.note.grid(row=3, columnspan=3)
        
    def updateprice(self):
        connection = CampBX(self)
        price = connection.xticker_print()
        # UPdate Labels
        self.priceticker.config(text=price["Last Trade"])
        self.priceticker.update()
        self.bidticker.config(text=price["Best Bid"])
        self.bidticker.update()
        self.askticker.config(text=price["Best Ask"])
        self.askticker.update()
        
        
        return