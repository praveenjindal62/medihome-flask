from web.views.interfaces.ViewInterface import ViewInterface
import re

urlObjlList=[]

class url:
    __url_pattern=""
    __request_method=""
    __targetView=ViewInterface()
    
    def __init__(self,url_pattern,request_method,targetView):
        self.__url_pattern=url_pattern
        self.__targetView=targetView
        self.__request_method=request_method
        if(request_method=="" or request_method=="None"):
            self.__request_method="GET"

    def setURLResolver(self,url_pattern,request_method,targetView):
        self.__url_pattern=url_pattern
        self.__targetView=targetView
        self.__request_method=request_method

    def match(self,_url_string,request_method):
        if(re.match(self.__url_pattern,_url_string) and self.__request_method==request_method):
            return True
    
    def getTargetView(self):
        return self.__targetView
    def getRequestMethod(self):
        return self.__request_method
    def getURLPattern(self):
        return self.__url_pattern

def resolveURL(url_string,request_method):
    for urlObj in urlObjlList:
        if(urlObj.match(url_string,request_method)):
            return urlObj.getTargetView()
    print('URL STRING IS '+ url_string)
    raise Exception("Could not resolve url - " + url_string+ ' # request method - '+ request_method)    

def addURLToList(url_pattern,request_method,view):
    urlObjlList.append(url(url_pattern,request_method,view))

def printURLList():
    for urlObj in urlObjlList:
        print("URL Pattern %s - Request-Method %s - View - %s"%(urlObj.getURLPattern(),urlObj.getRequestMethod(),urlObj.getTargetView().__class__.__name__))