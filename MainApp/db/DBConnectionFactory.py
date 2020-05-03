from pymongo import MongoClient
import os
class MongoConnection:
    __db_connection=None
    connectionSuccessful=False
    def __find(self,_collection,_query):
        return _collection.find(_query)

    def __add(self,_collection,_query):
        return _collection.insert(_query)

    def __delete(self,_collection,_query):
        return _collection.remove(_query)

    def __update(self,_collection,_query):
        return _collection.update(_query)

    def run(self,_query):
        #_request=json.loads(_query)
        _request=_query
        _operation_type=_request['DO']
        _operation_db=_request['DBNAME']
        _operation_db_collection=_request['COLLECTION_NAME']
        _operation_query=_request['QUERY']
        _collection=self.__db_connection[_operation_db][_operation_db_collection]
        if _operation_type=='find':
            return self.__find(_collection,_operation_query)
        elif _operation_type=='add':
            return self.__add(_collection,_operation_query)
        elif _operation_type=='delete':
            return self.__delete(_collection,_operation_query)
        elif _operation_type=='update':
            return self.__update(_collection,_operation_query)
        else:
            _return_response={"_response":'InvalidQuery'}
            return _return_response

    def __createConnection(self,_db_params):
        #_db_params_parameter=json.loads(str(_db_params))
        _dbhost=_db_params['MongoHost']
        _dbport=_db_params['MongoPort']
        self.__db_connection=MongoClient('mongodb://'+_dbhost+'/'+_dbport)
        self.connectionSuccessful=True
    
    def createDBConnection(self,_db_params=None):
        if(_db_params != None):
            return self.__createConnection(_db_params)
        
        try:
            _OS_ENV_DBHOST=os.environ['MONGO_HOST']
        except KeyError:
            _OS_ENV_DBHOST=None
        except:
            raise("Unknown Error")

        try:
            _OS_ENV_DBPORT=os.environ['MONGO_PORT']
        except KeyError:
            _OS_ENV_DBPORT=None
        except:
            raise("Unknown Error")

        if(_OS_ENV_DBHOST=="" or _OS_ENV_DBHOST==None):
            print('MONGO_HOST environment variable is not set. Using default host 0.0.0.0')
            _OS_ENV_DBHOST="0.0.0.0"

        if(_OS_ENV_DBPORT=="" or _OS_ENV_DBPORT==None):
            print('MONGO_PORT environment variable is not set. Using default port 27017')
            _OS_ENV_DBPORT="27017"
            
        _db_conn_parameters={
            'MongoHost':_OS_ENV_DBHOST,
            'MongoPort':_OS_ENV_DBPORT
        }
        print('Creating DB Connection with below parameters')
        print(_db_conn_parameters)
        self.__createConnection(_db_conn_parameters)

    def __init__(self):
        pass
        