from db.DBConnection import Connection
import json
class ModelInterface:
    dbname=""
    collectionname=""

    def find(self,json_query):
        dbQUery={
            "DO":"find",
            "DBNAME":self.dbname,
            "COLLECTION_NAME":self.collectionname,
            "QUERY":json_query
        }
        return Connection.run(dbQUery)

    def update(self,json_query):
        dbQUery={
            'DO':'update',
            'DBNAME':self.dbname,
            'COLLECTION_NAME':self.collectionname,
            'QUERY':json_query
        }
        return Connection.run(dbQUery)

    def insert(self,json_query):
        dbQUery={
            'DO':'add',
            'DBNAME':self.dbname,
            'COLLECTION_NAME':self.collectionname,
            'QUERY':json_query
        }
        return Connection.run(dbQUery)        
    
    def delete(self,json_query):
        dbQUery={
            'DO':'delete',
            'DBNAME':self.dbname,
            'COLLECTION_NAME':self.collectionname,
            'QUERY':json_query
        }
        return Connection.run(dbQUery)  
    