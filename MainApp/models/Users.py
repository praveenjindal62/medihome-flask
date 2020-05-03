from models.interface.modelInterface import ModelInterface
class Users(ModelInterface):
    def __init__(self):
        self.dbname="medihome"
        self.collectionname="Users"
