#WootPy
#A python wrapper for the Woot API

import settings

import urllib.request,json

class event:
    def __init__(self,Id,Title=None):
        pass

class woot:
    
    def __init__(self):
        pass
    
    def getRequest(self,req):#Generic function to send GET requests and handle error
        try:
            url_request = urllib.request.Request(req)
            response = urllib.request.urlopen(url_request)
            json_data = response.read().decode('utf-8')
            data = json.loads(json_data)
            return data
        except:
            print(urllib.error.HTTPError)
            print(urllib.error.UrlError)
            return False

    def getWoot(self,select=None,eventType=None,site=None,id=None):
        req = 'http://api.woot.com/2/events'
        #convert to lists
        if select:
            select = [select]
        if eventType:
            eventType = [eventType]
        if site:
            site = [site]
            
        if id:
            req += '/'
            req += str(id)
        req += '.json?key='
        req += settings.API_key
        if select:
            req += '&select='
            for s in select:
                req += str(s)
                req += ','
            req = req[:-1]#Remove the trailing ','
        if eventType:
            req += '&eventType='
            for s in eventType:
                req += str(s)
                req += ','
            req = req[:-1]#Remove the trailing ','
        if site:
            req += '&site='
            for s in site:
                req += str(s)
                req += ','
            req = req[:-1]#Remove the trailing ','
        return self.getRequest(req)
        
    def getAll(self):#Gets a list of all titles (and IDs) currently active on Woot
        #TODO find if WootOff or Daily
        return self.getWoot()

    def checkBOC(self,data=None):
        if data == None:
            data = self.getAll()
        for wootOff in data:
            for offer in wootOff['Offers']:
                search_title = offer['Title'].lower()
                if "boc" in search_title or 'bag of crap' in search_title:
                    return offer
        return False