from flask import Flask,request,session
from web.url.loadurl import loadurllist
from web.url.url import resolveURL
from db.DBConnection import Connection
import secrets
#from db.db import DBConnection
app=Flask(__name__)
app.secret_key=secrets.token_urlsafe(32)
loadurllist()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>',methods=['GET','POST'])
def mainPage(path):
    obj=resolveURL(path,request.method)()
    return obj.process(request,session)

if(__name__=='__main__'):
    #DBConnectionobj=db.DBConnection()
    #db.connectionObj=DBConnectionobj.createMongoConnection()
    app.run(host='0.0.0.0',port=5005)
