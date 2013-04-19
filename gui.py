from tkinter import *
from tkinter.ttk import *
import datetime
import os
from campbx import CampBX

class GUI:
    
    connection = CampBX()
    currentmid = 0
    currentbid = 0
    currentask = 0
    
    def __init__(self, master):

        self.upfromme=master

        
        frame = Frame(master)
        frame.grid(column=0, row=0)
        
        tabone = Notebook(frame)
        tabone.add(frame, text="Main Data")
        tabone.grid(row=0, column=10)
        
        # Adding Content Frames
        self.cmframe = LabelFrame(frame, text="Current Market")
        self.histframe = LabelFrame(frame, text="Historical Data")
        self.cmframe.grid(column=0)
        self.histframe.grid(row=0, column=1)
        
        self.pressframe = LabelFrame(frame, text="Market Pressure")
        self.pressframe.grid(row=1, columnspan=2)

        #Menu
        self.menu = Menu(master)
        master.config(menu = self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Exit", command=quit)
        
        
        #draw frames
        self.drawcm()
        self.drawhist()
        self.drawpress()
        
        # Set update loop in motion
        self.update()
        self.updatehistory()
        
    def drawpress(self):
        self.currentmidlbl = Label(self.pressframe, text="Median...")
        self.biddesc = Label(self.pressframe, text="Bids")
        self.askdesc = Label(self.pressframe, text="Asks")
        self.currentmidlbl.grid(row=0, columnspan=6)
        self.biddesc.grid(row=1, columnspan=2)
        self.askdesc.grid(row=1, column=3, columnspan=2)
        
        self.bidusddesc = Label(self.pressframe, text="Below by $")
        self.bidbtcdesc = Label(self.pressframe, text="BTC Vol")
        self.bidnumdesc = Label(self.pressframe, text="Orders")
        self.bidusddesc.grid(row=2, column=0)
        self.bidbtcdesc.grid(row=2, column=1)
        self.bidnumdesc.grid(row=2, column=2)
        self.askusddesc = Label(self.pressframe, text="Above by $")
        self.askbtcdesc = Label(self.pressframe, text="BTC Vol")
        self.asknumdesc = Label(self.pressframe, text="Orders")
        self.asknumdesc.grid(row=2, column=5)
        self.askusddesc.grid(row=2, column=3)
        self.askbtcdesc.grid(row=2, column=4)
        
        # Bids USD
        self.bidlt1  = Label(self.pressframe, text="$ 01")
        self.bidlt1.grid(row=3, column=0)
        self.bidlt5  = Label(self.pressframe, text="$ 05")
        self.bidlt5.grid(row=4, column=0)
        self.bidlt10 = Label(self.pressframe, text="$ 10")
        self.bidlt10.grid(row=5, column=0)
        self.bidlt25 = Label(self.pressframe, text="$ 25")
        self.bidlt25.grid(row=6, column=0)
        self.bidlt50 = Label(self.pressframe, text="$ 50")
        self.bidlt50.grid(row=7, column=0)
        
        # Bids Vol
        self.bidv1  = Label(self.pressframe, text="Vol BTC")
        self.bidv1.grid(row=3, column=1)
        self.bidv5  = Label(self.pressframe, text="Vol BTC")
        self.bidv5.grid(row=4, column=1)
        self.bidv10 = Label(self.pressframe, text="Vol BTC")
        self.bidv10.grid(row=5, column=1)
        self.bidv25 = Label(self.pressframe, text="Vol BTC")
        self.bidv25.grid(row=6, column=1)
        self.bidv50 = Label(self.pressframe, text="Vol BTC")
        self.bidv50.grid(row=7, column=1)
        
        # Bids Num
        self.bidn1 = Label(self.pressframe, text="#")
        self.bidn1.grid(row=3, column=2)
        self.bidn5 = Label(self.pressframe, text="#")
        self.bidn5.grid(row=4, column=2)
        self.bidn10 = Label(self.pressframe, text="#")
        self.bidn10.grid(row=5, column=2)
        self.bidn25 = Label(self.pressframe, text="#")
        self.bidn25.grid(row=6, column=2)
        self.bidn50 = Label(self.pressframe, text="#")
        self.bidn50.grid(row=7, column=2)
        
        
        #Ask Dollars
        self.askgt1  = Label(self.pressframe, text="$ 01")
        self.askgt1.grid(row=3, column=3)
        self.askgt5  = Label(self.pressframe, text="$ 05")
        self.askgt5.grid(row=4, column=3)
        self.askgt10 = Label(self.pressframe, text="$ 10")
        self.askgt10.grid(row=5, column=3)
        self.askgt25 = Label(self.pressframe, text="$ 25")
        self.askgt25.grid(row=6, column=3)
        self.askgt50 = Label(self.pressframe, text="$ 50")
        self.askgt50.grid(row=7, column=3)
        
        #Ask Volume
        self.askv1  = Label(self.pressframe, text="Vol BTC")
        self.askv1.grid(row=3, column=4)
        self.askv5  = Label(self.pressframe, text="Vol BTC")
        self.askv5.grid(row=4, column=4)
        self.askv10  = Label(self.pressframe, text="Vol BTC")
        self.askv10.grid(row=5, column=4)
        self.askv25  = Label(self.pressframe, text="Vol BTC")
        self.askv25.grid(row=6, column=4)
        self.askv50  = Label(self.pressframe, text="Vol BTC")
        self.askv50.grid(row=7, column=4)
        
        #Ask Numbers
        self.askn1 = Label(self.pressframe, text="#")
        self.askn1.grid(row=3, column=5)
        self.askn5 = Label(self.pressframe, text="#")
        self.askn5.grid(row=4, column=5)
        self.askn10 = Label(self.pressframe, text="#")
        self.askn10.grid(row=5, column=5)
        self.askn25 = Label(self.pressframe, text="#")
        self.askn25.grid(row=6, column=5)
        self.askn50 = Label(self.pressframe, text="#")
        self.askn50.grid(row=7, column=5)
        
        return
        
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
        
        self.currentbid = float(price["Best Bid"])
        self.bidticker.config(text=price["Best Bid"])
        self.bidticker.update()
        
        self.currentask = float(price["Best Ask"])
        self.askticker.config(text=price["Best Ask"])
        self.askticker.update()
        
        self.currentmid = (self.currentbid + self.currentask) / 2.0
        self.currentmidlbl.config(text=self.currentmid)
        self.currentmidlbl.update()
        
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
        
        analysis = self.analyzedepth(orders)
        self.updateanalyzedepth(analysis)
        
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
        
    def analyzedepth(self, ordertable):
        # Definition "Delta $" : [ Orders, BTC ] 
        pressure= { "+1" : [0,0] , "+5" : [0,0], "+10" : [0,0], "+25" : [0,0], "+50" : [0,0],\
                    "-1" : [0,0] , "-5" : [0,0], "-10" : [0,0], "-25" : [0,0], "-50" : [0,0]}
        
        # How To:
        #print (pressure)
        #pressure["+1/2"][0]+=1
        #pressure["+1/2"][1]+=3
        #print (pressure)
        
        for i in ordertable["Asks"][::-1] :
            distance = float(i[0]) - float(self.currentmid)
            if distance < 1:
                pressure["+1"][0]+=1
                pressure["+1"][1]+=i[1]
            if distance < 5:
                pressure["+5"][0]+=1
                pressure["+5"][1]+=i[1]
            if distance < 10:
                pressure["+10"][0]+=1
                pressure["+10"][1]+=i[1]
            if distance < 25:
                pressure["+25"][0]+=1
                pressure["+25"][1]+=i[1]
            if distance < 50:
                pressure["+50"][0]+=1
                pressure["+50"][1]+=i[1]
                
        for i in ordertable["Bids"][:] :
            distance = float(self.currentmid) - float(i[0])
            if distance < 1:
                pressure["-1"][0]+=1
                pressure["-1"][1]+=i[1]
            if distance < 5:
                pressure["-5"][0]+=1
                pressure["-5"][1]+=i[1]
            if distance < 10:
                pressure["-10"][0]+=1
                pressure["-10"][1]+=i[1]
            if distance < 25:
                pressure["-25"][0]+=1
                pressure["-25"][1]+=i[1]
            if distance < 50:
                pressure["-50"][0]+=1
                pressure["-50"][1]+=i[1]
        
        return pressure
        
    def updateanalyzedepth(self, pressure):
        
        self.bidv1.config(text=round(pressure["-1"][1],3))
        self.bidv1.update()
        self.bidv5.config(text=round(pressure["-5"][1],3))
        self.bidv5.update()
        self.bidv10.config(text=round(pressure["-10"][1],3))
        self.bidv10.update()
        self.bidv25.config(text=round(pressure["-25"][1],3))
        self.bidv25.update()
        self.bidv50.config(text=round(pressure["-50"][1],3))
        self.bidv50.update()
        
        self.bidn1.config(text=pressure["-1"][0])
        self.bidn1.update()
        self.bidn5.config(text=pressure["-5"][0])
        self.bidn5.update()
        self.bidn10.config(text=pressure["-10"][0])
        self.bidn10.update()
        self.bidn25.config(text=pressure["-25"][0])
        self.bidn25.update()
        self.bidn50.config(text=pressure["-50"][0])
        self.bidn50.update()
        
        self.askv1.config(text=round(pressure["+1"][1],3))
        self.askv1.update()
        self.askv5.config(text=round(pressure["+5"][1],3))
        self.askv5.update()
        self.askv10.config(text=round(pressure["+10"][1],3))
        self.askv10.update()
        self.askv25.config(text=round(pressure["+25"][1],3))
        self.askv25.update()
        self.askv50.config(text=round(pressure["+50"][1],3))
        self.askv50.update()
        
        self.askn1.config(text=pressure["+1"][0])
        self.askn1.update()
        self.askn5.config(text=pressure["+5"][0]) 
        self.askn5.update()
        self.askn10.config(text=pressure["+10"][0])
        self.askn10.update()
        self.askn25.config(text=pressure["+25"][0])
        self.askn25.update()
        self.askn50.config(text=pressure["+50"][0])
        self.askn50.update()
        
        return
      