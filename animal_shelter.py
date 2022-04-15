from pymongo import MongoClient
from bson.objectid import ObjectId

class animal_shelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.

        self.client = MongoClient('mongodb://localhost:56377/AAC' % (username,password))
        self.database = self.client['AAC']


# Complete this create method to implement the C in CRUD.(create)
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True# data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.(read)
    def read_all(self,data=None):
        if data:
            cursor = self.database.animals.find(data,{"_id": False})
        else:
            cursor = self.database.animals.find({},{"_id": False})
        return cursor

    def read(self,data):
        return self.database.animals.find_one(data, {"_id": False})
    
#Method to implement the U in CRUD (update)
    def update_one(self):
        query = {"animal_id": "B000001"}
        value = {"$set": {"animal_id": "B000003"}}
        return self.collection.update_one(query,value)
    #update many
    def update_many(self):
        cursor = self.database.animals.update_many({"animal_id": "B000001"},{"$set":{"animal_id": "B000003"}})
        return cursor


#Method to implement the D in CRUD (delete)
    #delete one
    def delete_one(self):
        return self.database.animals.delete_one({"animal_id": "B000003"})
    #delete many
    def delete_many(self):
        cursor = self.database.animals.delete_many({"animal_id": "B000003"})
        return cursor