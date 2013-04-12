import json
import urllib.request
import logging
import time
import datetime


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
        now = int(time.time())
        hourago = now - 60*30
        xhistoryurl = "http://bitcoincharts.com/t/trades.csv?symbol=CBXUSD&end="+str(hourago)
        print(xhistoryurl)
        request = urllib.request.Request(xhistoryurl)
        response = urllib.request.urlopen(request)
        print ((response.read().decode('utf-8')))
        
        return