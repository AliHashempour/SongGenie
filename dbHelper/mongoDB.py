import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()


def connect_to_mongo():
    mongo_uri = os.getenv('MONGO_URI')
    db_name = os.getenv('MONGO_DB_NAME')
    collection_name = os.getenv('MONGO_COLLECTION_NAME')

    cluster = MongoClient(mongo_uri)
    db = cluster[db_name]
    collection = db[collection_name]
    return collection


def insert_to_db(_id, user_email, status="pending"):
    collection = connect_to_mongo()
    collection.insert_one({"_id": _id, "email": user_email, "status": status, "songId": None})


def update_songId(_id, song_id):
    collection = connect_to_mongo()
    update = {
        "$set": {
            "songId": song_id,
            "status": "ready"
        }
    }
    result = collection.update_one({'_id': _id}, update=update)
    if result.modified_count > 0:
        print(f"Document {_id} updated successfully to ready")


def select_ready_records():
    collection = connect_to_mongo()
    res = collection.find({"status": "ready"})
    return list(res)


def update_status(_id, status):
    try:
        collection = connect_to_mongo()
        update = {
            "$set": {
                "status": status,
            }
        }

        result = collection.update_one({'_id': _id}, update=update)

        if result.modified_count > 0:
            print(f"Document {_id} updated successfully to {status}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
