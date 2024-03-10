import boto3
import logging
from botocore.exceptions import ClientError


def get_credentials():
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url='https://alicloudhw1.s3.ir-thr-at1.arvanstorage.ir',
            aws_access_key_id='f57cb26f-117e-4681-8c03-2cae33b1b3bb',
            aws_secret_access_key='3e0cbadd4eb896ba9e375bd0f8d117b113df4dccdbd19daaaa8375bcd45e6948'
        )
        return s3_resource

    except Exception as exc:
        logging.error(exc)


def insert_to_storage(file_path, file_name):
    try:
        s3_resource = get_credentials()
        bucket = s3_resource.Bucket('alicloudhw1')
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
