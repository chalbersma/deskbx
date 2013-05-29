import json
import urllib.request
import logging
import time
import datetime
import csv


class CampBX(object):
    username = None
    password = None
    api_url = "https://campbx.com/api/"
    #hist_url = "http://bitcoincharts.com/t/trades.csv?symbol=SYMBOL[&start=UNIXTIME][&end=UNIXTIME]"
    log = None

    def __init__(self, master):
        return
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password    
    
    def xticker_print(self):
        xtickerurl = self.api_url + "xticker.php"
        request = urllib.request.Request(xtickerurl)
        response = urllib.request.urlopen(request)
        xjson = json.loads((response.read().decode('utf-8')))
        return xjson
    
    def xdepth_print(self):
        xdepthurl = self.api_url + "xdepth.php"
        request = urllib.request.Request(xdepthurl)
        response = urllib.request.urlopen(request)
        xdepth = json.loads((response.read().decode('utf-8')))
        return xdepth
        
    def historical(self):
        #Pulls information from bitcoincharts.com
        now = int(time.time())
        hourago = now - 60*30
        xhistoryurl = "http://bitcoincharts.com/t/markets.json"
        request = urllib.request.Request(xhistoryurl)
        try:
            response = urllib.request.urlopen(request)
        except urllib.request.URLError as e:
            print ("Couldn't Pull Data")
        else:
            xhistory = json.loads((response.read().decode('utf-8')))
            for i in xhistory[:] : 
                if (i['symbol'] == 'cbxUSD'):
                    camphistory=i
        return camphistory
        
    def afunds(self):
        afundsurl = self.api_url + "myfunds.php"
        mecreds = { "user" : self.username , "pass" : self.password }
        data = urllib.parse.urlencode(mecreds)
        bindata = data.encode('utf-8')
        request = urllib.request.Request(afundsurl, bindata)
        response = urllib.request.urlopen(request)
        afunds = json.loads((response.read().decode('utf-8')))
        print(afunds)
        return afunds
        
    def setcred(self, creds):
        self.username = creds["username"]
        self.password = creds["password"]
        
        return
        