from storageHelper.s3 import download_object


class SongWorker:
    def __init__(self, message):
        self.msg = message

    def process_message(self):
        download_object(self.msg)


