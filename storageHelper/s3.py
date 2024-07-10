import os
from dotenv import load_dotenv
import boto3
import logging
from botocore.exceptions import ClientError

load_dotenv()


def get_credentials():
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=os.getenv('ENDPOINT_URL'),
            aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY')
        )
        return s3_resource

    except Exception as exc:
        logging.error(exc)


def insert_to_storage(file_path, file_name):
    try:
        s3_resource = get_credentials()
        bucket = s3_resource.Bucket(os.getenv('BUCKET_NAME'))
        file_path = file_path
        object_name = file_name

        with open(file_path, "rb") as file:
            bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )
    except ClientError as e:
        logging.error(e)


def download_object(hash_obj):
    try:
        s3_resource = get_credentials()
        bucket = s3_resource.Bucket(os.getenv('BUCKET_NAME'))

        object_name = f'{hash_obj}.mp3'
        root_directory = os.getenv('ROOT_DIRECTORY')
        download_path = os.path.join(root_directory, "savedFiles", object_name)

        bucket.download_file(
            hash_obj,
            download_path
        )
        print(f"file saved in : {download_path}")
        return object_name

    except ClientError as e:
        logging.error(e)
