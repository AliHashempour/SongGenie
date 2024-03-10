import os

import requests


class ShazamWorker:
    def __init__(self, file_name):
        self.file = file_name
        self.url = self.get_url()
        self.headers = self.get_headers()

    def get_url(self):
        return "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

    def get_headers(self):

        headers = {
            "X-RapidAPI-Key": "41db0ae0dbmshb4369a7209144dap1bf6e5jsn8938fa198638",
            "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
        }
        return headers

    def get_file_path(self):
        root_directory = 'D:\programming_codes\python\myPythoneProjects\cloud-hw1'
        file_path = os.path.join(root_directory, "savedFiles", self.file)
        return file_path

    def send_request_to_shazam(self):

        file_path = self.get_file_path()

        with open(file_path, 'rb') as file:
            # Create a dictionary containing the file to be sent
            files = {'upload_file': file}
            response = requests.post(self.url, files=files, headers=self.headers)

        if response.status_code == 200:
            print('File uploaded successfully!')
            res = response.json()
            title, artist = res['track']['title'], res['track']['subtitle']
            return title, artist
        else:
            print('Failed to upload file:', response.text)
