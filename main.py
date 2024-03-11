from flask import Flask, request
from utils.general import generate_hash, save_file
from dbHelper.mongoDB import insert_to_db, update_status
from rabbitHelper.rabbitMQ import *
from storageHelper.s3 import *

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    response = {}
    email, music_file = request.form.get('email'), request.files['music']
    hashed_name = generate_hash()
    try:
        file_name, file_path = save_file(music_file)
        insert_to_storage(file_path=file_path, file_name=hashed_name)
        response["s3"] = True
        insert_to_db(_id=hashed_name, user_email=email)
        response["mongo"] = True
        produce_on_rabbit(msg=hashed_name)
        response["rabbitMQ"] = True

    except Exception as e:
        print(f"error in progress : {e}")
        update_status(_id=hashed_name, status="Failure")

    return response


if __name__ == '__main__':
    app.run(debug=True)
