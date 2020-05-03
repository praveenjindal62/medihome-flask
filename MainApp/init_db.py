from pymongo import MongoClient

host='0.0.0.0'
port='27017'
mongo_client=MongoClient('mongodb://'+host+'/'+port)

db=mongo_client.mymongodb
coll=db.med
