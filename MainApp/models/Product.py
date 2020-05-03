from models.interface.modelInterface import ModelInterface
class Product(ModelInterface):
    def __init__(self):
        self.dbname="medihome"
        self.collectionname="Product"
    def findAll(self,_search_string):
        return self.find({"$text": {"$search": _search_string}})