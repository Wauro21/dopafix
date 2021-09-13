import pymongo
import json
from Sampleclass import Sampleclass
from pprint import pprint
# Replace the uri string with your MongoDB deployment's connection string.
conn_str = 'mongodb://localhost:27017/'#"mongodb://
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

##-------------------- CRUD Operations

# Creation: Takes a Python Dictionary and inserts it onto the desired collection. Returns the generated ID
def sampleCreate(name, age, collection):
    toCreate = Sampleclass(name,age, None)
    rId = collection.insert_one(toCreate.__dict__)
    return rId

# Read: Takes an _id and search for the corresponding doc in the DB, retrieves the information a return an Object of Sampleclass
def sampleRead(collection, _id):
    result = collection.find_one({"_id":_id})
    return result

try:
    #print(client.server_info())
    db = client.dopafix_ns
    #print(db)
    collection = db.testing

    # C
    r_id = sampleCreate("Mauricio","24", collection).inserted_id

    # R
    pprint(sampleRead(collection, r_id))
except Exception as e:
    print(e)
