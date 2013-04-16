from tkinter import *
#from tkinter.ttk import *
import datetime
import os
from campbx import CampBX

class GUI:
    
    connection = CampBX()

    def __init__(self, master):

        self.upfromme=master

        frame = Frame(master)
        frame.grid(column=0, row=0)
        
        # Adding Content Frames
        self.cmframe = LabelFrame(frame, text="Current Market", padx=5, pady=5)
        self.histframe = LabelFrame(frame, text="Historical Data", padx=5, pady=5)
        self.cmframe.grid(column=0)
        self.histframe.grid(row=0, column=1)

        #Menu
        self.menu = Menu(master)
        master.config(menu = self.menu)

        #draw frames
        self.drawcm()
        self.drawhist()
        # Set update loop in motion
        self.update()
        self.updatehistory()
    def drawcm(self):
        #Description Label
        self.pricetickerdesc=Label(self.cmframe,text="Price")
        self.pricetickerdesc.grid(row=0, sticky='W')
        self.biddesc=Label(self.cmframe,text="Bid")
        self.biddesc.grid(row=0,column=1, columnspan=2)
        self.biddesc=Label(self.cmframe,text="Ask")
        self.biddesc.grid(row=0,column=3, sticky='E')
        
        #Current Orders Label
        self.bidsdesc=Label(self.cmframe,text="Open Bids")
        self.bidsdesc.grid(row=2, column=0, columnspan=2, sticky='W')
        self.asksdesc=Label(self.cmframe,text="Open Asks")
        self.asksdesc.grid(row=2, column=2, columnspan=2, sticky='E')
    
        #Current Price Label
        self.priceticker=Label(self.cmframe,text="Last...")
        self.priceticker.grid(row=1, sticky='W')
        self.bidticker=Label(self.cmframe,text="Bid...")
        self.bidticker.grid(row=1,column=1, columnspan=2)
        self.askticker=Label(self.cmframe,text="Ask...")
        self.askticker.grid(row=1,column=3, sticky='E')
        
        
        #Top 3 Bids
        self.bids1=Label(self.cmframe,text="$0x0")
        self.bids1.grid(row=3, column=0, columnspan=2, sticky='W')
        self.bids2=Label(self.cmframe,text="$0x0")
        self.bids2.grid(row=4, column=0, columnspan=2, sticky='W')
        self.bids3=Label(self.cmframe,text="$0x0")
        self.bids3.grid(row=5, column=0, columnspan=2, sticky='W')
        
        #Top 3 Asks
        self.asks1=Label(self.cmframe,text="$0x0")
        self.asks1.grid(row=3, column=2, columnspan=2, sticky='E')
        self.asks2=Label(self.cmframe,text="$0x0")
        self.asks2.grid(row=4, column=2, columnspan=2, sticky='E')
        self.asks3=Label(self.cmframe,text="$0x0")
        self.asks3.grid(row=5, column=2, columnspan=2, sticky='E')
        
        #No Longer Needed
        #Update Button (Runs Update)
        #self.priceupdate=Button(frame, text="Update", command=self.update())
        #self.priceupdate.grid(row=8, columnspan=4)
        
        self.note=Label(self.cmframe,text="Updated Every Minute\nfrom Campbx.com")
        self.note.grid(row=8, columnspan=4)
        
        return
        
    def drawhist(self):
        # Historical Data
        self.historydesc=Label(self.histframe,text="Market Data")
        self.historydesc.grid(row=0, columnspan=4)
        
        # Items
        self.avg=Label(self.histframe,text="Trade 1")
        self.avgdesc=Label(self.histframe,text="24HR AVG")
        self.avgdesc.grid(row=1, column=0, sticky='W')
        self.avg.grid(row=1, column=2, columnspan=2, sticky='E')
        
        self.vol=Label(self.histframe,text="Trade 1")
        self.voldesc=Label(self.histframe,text="VOL USD")
        self.voldesc.grid(row=2, column=0, sticky='W')
        self.vol.grid(row=2, column=2, columnspan=2, sticky='E')
        
        self.high=Label(self.histframe,text="Trade 1")
        self.highdesc=Label(self.histframe,text="HIGH")
        self.highdesc.grid(row=3, column=0, sticky='W')
        self.high.grid(row=3, column=2, columnspan=2, sticky='E')
        
        self.low=Label(self.histframe,text="Trade 1")
        self.lowdesc=Label(self.histframe,text="LOW")
        self.lowdesc.grid(row=4, column=0, sticky='W')
        self.low.grid(row=4, column=2, columnspan=2, sticky='E')
        
        self.volBTC=Label(self.histframe,text="Trade 1")
        self.volBTCdesc=Label(self.histframe,text="VOL BTC")
        self.volBTCdesc.grid(row=5, column=0, sticky='W')
        self.volBTC.grid(row=5, column=2, columnspan=2, sticky='E')
        

        
        #Market Button (Runs Updatehistory)
        #self.marketupdate=Button(self.histframe,text="Update", command=self.updatehistory())
        #self.marketupdate.grid(row=8, column=0, columnspan=4)
        
        self.note2=Label(self.histframe,text="Updated Every 16 Minutes \nfrom bitcoincharts.com")
        self.note2.grid(row=8, column=0, columnspan=4)

        return
        
        
    def update(self):
        print ("Updating Prices")
        self.updateprice()
        self.updateorders()
        self.upfromme.after(60000, self.update)
        return
        
        
    def updateprice(self):
        self.connection = CampBX(self)
        price = self.connection.xticker_print()
        # UPdate Labels
        self.priceticker.config(text=price["Last Trade"])
        self.priceticker.update()
        self.bidticker.config(text=price["Best Bid"])
        self.bidticker.update()
        self.askticker.config(text=price["Best Ask"])
        self.askticker.update()
        
        
        return
        
    def updateorders(self):
        self.connection = CampBX(self)
        orders = self.connection.xdepth_print()
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
        print("Updating History")
        self.connection = CampBX(self)
        history = self.connection.historical()
        self.avg.config(text="$" + str(round(history["avg"],2)))
        self.avg.update()
        self.vol.config(text="$" + str(round(history["currency_volume"],2)))
        self.vol.update()
        self.high.config(text="$" + str(round(history["high"],2)))
        self.high.update()
        self.low.config(text="$" + str(round(history["low"],2)))
        self.low.update()
        self.volBTC.config(text=str(round(history["volume"],2)) + "BTC")
        self.volBTC.update()
        self.upfromme.after(960000, self.updatehistory)
        
        return
        