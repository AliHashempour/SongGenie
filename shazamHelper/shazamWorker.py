import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()


class ShazamWorker:
    def __init__(self, file_name):
        self.file = file_name
        self.url = self.get_url()
        self.headers = self.get_headers()

    def get_url(self):
        return "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

    def get_headers(self):
        headers = {
            "X-RapidAPI-Key": os.getenv('SHAZAM_API_KEY'),
            "X-RapidAPI-Host": os.getenv('SHAZAM_API_HOST')
        }
        return headers

    def get_file_path(self):
        root_directory = os.getenv('ROOT_DIRECTORY')
        file_path = os.path.join(root_directory, "savedFiles", self.file)
        return file_path

    def send_request_to_shazam(self):
        file_path = self.get_file_path()

        with open(file_path, 'rb') as file:
            files = {'upload_file': file}
            response = requests.post(self.url, files=files, headers=self.headers)

        if response.status_code == 200:
            print('File uploaded successfully!')
            res = response.json()
            title, artist = res['track']['title'], res['track']['subtitle']
            return title, artist
        else:
            print('Failed to upload file:', response.text)
