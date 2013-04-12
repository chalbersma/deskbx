import json
import urllib.request

class CampBX(object):
    def __init__(self, master):
        """Camp BX API Class"""
        self.username = None
        self.password = None
        self.api_url = 'https://campbx.com/api/'
        self.log = None
        
    def xticker_print(self):
        xtickerurl = self.api_url + "xticker.php"
        request = urllib.request.Request(xtickerurl)
        response = urllib.request.urlopen(request)
        xjson = json.loads((response.read().decode('utf-8')))
        return xjson
        