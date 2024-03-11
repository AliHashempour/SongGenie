from pymongo import MongoClient


def connect_to_mongo():
    cluster = MongoClient("mongodb+srv://alihashempour:1234@cluster0.qicseon.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["firstDB"]
    collection = db["request"]
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
        print(f"Document {_id} updated successfully.")


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
            print(f"Document {_id} updated successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
