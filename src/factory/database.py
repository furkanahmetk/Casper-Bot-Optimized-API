from datetime import datetime
import pymongo
from bson import ObjectId
from pymongo import  UpdateOne

"""
An object for wrapping database operations. This is a static object that its init function should be called once to
keep database connection number 1. 
This object includes functions for updating, creating and deleting objects from spesific collection.
"""

class Database(object):
    @staticmethod
    def init(uri,db_name):
        client = pymongo.MongoClient(uri)
        Database.DB = client[db_name]
        #This is bad practice will change in the next version
        Database.DB['validators'].create_index('public_key',unique=True)

    @staticmethod
    def create_index(collection_name,index_name):
        Database.DB[collection_name].create_index(index_name,unique=True)

    @staticmethod
    def insert(element, collection_name):
        create_and_update_time =  datetime.now()
        element["created"] = create_and_update_time
        element["updated"] = create_and_update_time
        inserted = Database.DB[collection_name].insert_one(element)  # insert data to db
        return str(inserted.inserted_id)
        
    @staticmethod
    def insert_many(list_of_element,collection_name):
        create_and_update_time =  datetime.now()
        for i in range(len(list_of_element)):
            list_of_element[i]["created"] = create_and_update_time
            list_of_element[i]["updated"] = create_and_update_time
        Database.DB[collection_name].insert_many(list_of_element)  # insert data to db
        return 'success'


    @staticmethod
    def find( criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):  

        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])

        found = Database.DB[collection_name].find(filter=criteria, projection=projection, limit=limit, sort=sort)

        if cursor:
            return found

        found = list(found)

        for i in range(len(found)):  # to serialize object id need to convert string
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    @staticmethod
    def find_by_id( id, collection_name):
        found = Database.DB[collection_name].find_one({"_id": ObjectId(id)})
        
        if found is None:
            return not found
        
        if "_id" in found:
             found["_id"] = str(found["_id"])

        return found

    @staticmethod
    def update(id, element, collection_name):
        criteria = {"_id": ObjectId(id)}

        element["updated"] = datetime.now()
        set_obj = {"$set": element}  # update value

        updated = Database.DB[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    @staticmethod
    def update_many( elements, collection_name):
        update_time =  datetime.now()
        collection = Database.DB[collection_name]
        operations = []
        for item in elements:
            # process in bulk
            item['updated'] = update_time
            item['_id'] = ObjectId(item['_id'])
            operations.append(UpdateOne({ '_id': ObjectId(item['_id']) },{ '$set': item }))
        result = collection.bulk_write(operations)
        print(result)
        return 'success'

    @staticmethod
    def delete( id, collection_name):
        deleted = Database.DB[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)