from django.conf import settings
import pymongo
from bson import ObjectId


class Repository:
    def __init__(self, collection_name) -> None:
        self.collection = collection_name

    def getConnection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection

    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection

    def getUserByNameAndPassword(self, username, password):
        document = self.getCollection().find_one(
            {"username": username, "password": password}
        )
        return document

    def getByAttribute(self, attribute, value):
        document = self.getCollection().find_one({f"{attribute}": value})

    def delete(self, document) -> None:
        self.getCollection().delete_one(document)

    def deleteAll(self) -> None:
        self.getCollection().delete_many({})

    def findOneById(self, id):
        id = ObjectId(id)
        document = self.getCollection().find_one({"_id": id})
        return document

    def getAll(self):
        document = self.getCollection().find({})
        return document

    def insert(self, document):
        document = self.getCollection().insert_one(document)
        return document

    def update(self, id, new_data):
        identifier = {"_id": ObjectId(id)}

        new_values = {"$set": new_data}

        response = self.getCollection().update_one(identifier, new_values)
        return response
