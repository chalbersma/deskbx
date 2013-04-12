import json
import urllib.request

class CampBX(object):
    def __init__(self, master):
        """Camp BX API Class"""
        username = None
        password = None
        api_url = 'https://campbx.com/api/'
        log = None

        jsonticker = json.load(urlopen("http://campbx.com/api/xticker.php"))
        jsonticker.dump
        
    def xticker_print(self):
        xtickerurl = api_url + "xticker.php"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        xjson = json.loads((response.read().decode('utf-8')))
        print ("Last Price")
        print (xjson["Last Trade"])
        return
        