import pymongo
import json
# Replace the uri string with your MongoDB deployment's connection string.
conn_str = 'mongodb://localhost:27017/'#"mongodb://
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

##-------------------- CRUD Operations

# Creation: Takes a Python Dictionary, converts it to JSON and inserts it onto the desired collection. Returns the generated ID
def sampleCreate():



try:
    #print(client.server_info())
    db = client.dopafix_ns
    #print(db)
    collection = db.testing
    file = collection.find_one()
    print(file['_id'])
    print("This is a new id:" + ObjectId())
except Exception:
    print("Unable to connect to the server.")
