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
        
        #Current Orders Label
        self.bidsdesc=Label(frame,text="Open Bids")
        self.bidsdesc.grid(row=4, column=0, columnspan=2)
        self.asksdesc=Label(frame,text="Open Asks")
        self.asksdesc.grid(row=4, column=2, columnspan=2)
        
        #Current Price Label
        self.priceticker=Label(frame,text="Last...")
        self.priceticker.grid(row=1)
        self.bidticker=Label(frame,text="Bid...")
        self.bidticker.grid(row=1,column=1)
        self.askticker=Label(frame,text="Ask...")
        self.askticker.grid(row=1,column=2)
        
        
        #Top 3 Bids
        self.bids1=Label(frame,text="$0x0")
        self.bids1.grid(row=5, column=0, columnspan=2)
        self.bids2=Label(frame,text="$0x0")
        self.bids2.grid(row=6, column=0, columnspan=2)
        self.bids3=Label(frame,text="$0x0")
        self.bids3.grid(row=7, column=0, columnspan=2)
        
        #Top 3 Asks
        self.asks1=Label(frame,text="$0x0")
        self.asks1.grid(row=5, column=2, columnspan=2)
        self.asks2=Label(frame,text="$0x0")
        self.asks2.grid(row=6, column=2, columnspan=2)
        self.asks3=Label(frame,text="$0x0")
        self.asks3.grid(row=7, column=2, columnspan=2)
        
        #Update Button (Runs Update)
        self.priceupdate=Button(frame, text="Update", command=self.update())
        self.priceupdate.grid(row=2, columnspan=3)
        
        self.note=Label(frame,text="Prices pulled from Campbx")
        self.note.grid(row=3, columnspan=3)
        
    def update(self):
        self.updateprice()
        self.updateorders()
        self.updatehistory()
        return
        
        
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
        
    def updateorders(self):
        connection = CampBX(self)
        orders = connection.xdepth_print()
        #   "$" + str(orders["Asks"][-2][0]) + " : " + str(orders["Asks"][-2][1]))
        #   Dollar Sign + Order in $ (rounded two 2) + Volume in Bitcoin (rounded two too
        #Update Price Tables
        self.asks1.config(text="$" + str(round(orders["Asks"][-1][0],2)) + " : " + str(round(orders["Asks"][-1][1],2)))
        self.asks1.update()
        self.asks2.config(text="$" + str(round(orders["Asks"][-2][0],2)) + " : " + str(round(orders["Asks"][-2][1],2)))
        self.asks2.update()
        self.asks3.config(text="$" + str(round(orders["Asks"][-3][0],2)) + " : " + str(round(orders["Asks"][-3][1],2)))
        self.asks3.update()
        
        #Update Bid Tables
        self.bids1.config(text="$" + str(round(orders["Bids"][0][0],2)) + " : " + str(round(orders["Bids"][0][1],2)))
        self.bids1.update()
        self.bids2.config(text="$" + str(round(orders["Bids"][1][0],2)) + " : " + str(round(orders["Bids"][1][1],2)))
        self.bids2.update()
        self.bids3.config(text="$" + str(round(orders["Bids"][2][0],2)) + " : " + str(round(orders["Bids"][2][1],2)))
        self.bids3.update()
        
        return
        
    def updatehistory(self):
        connection = CampBX(self)
        connection.historical()
        
        return
        