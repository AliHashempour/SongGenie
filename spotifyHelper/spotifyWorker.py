import os
from dotenv import load_dotenv
import requests

load_dotenv()


class SpotifyWorker:
    def __init__(self):
        self.search_url = self.get_search_url()
        self.search_headers = self.get_search_headers()
        self.recommend_url = self.get_recommend_url()
        self.recommend_headers = self.get_recommend_headers()

    def get_search_url(self):
        url = "https://spotify23.p.rapidapi.com/search/"
        return url

    def get_recommend_url(self):
        url = "https://spotify23.p.rapidapi.com/recommendations/"
        return url

    def get_search_headers(self):
        headers = {
            "X-RapidAPI-Key": os.getenv('SPOTIFY_API_KEY'),
            "X-RapidAPI-Host": os.getenv('SPOTIFY_API_HOST')
        }
        return headers

    def get_recommend_headers(self):
        headers = {
            "X-RapidAPI-Key": os.getenv('SPOTIFY_API_KEY'),
            "X-RapidAPI-Host": os.getenv('SPOTIFY_API_HOST')
        }
        return headers

    def send_search_request(self, search_song):
        querystring = {"q": f"{search_song}", "type": "tracks", "offset": "0", "limit": "1", "numberOfTopResults": "1"}
        response = requests.get(self.search_url, headers=self.search_headers, params=querystring)
        data = response.json()
        song_id = data['tracks']['items'][0]['data']['id']
        return song_id

    def send_recommend_request(self, song_id):
        querystring = {"limit": "1", "seed_tracks": song_id, }
        response = requests.get(self.recommend_url, headers=self.recommend_headers, params=querystring)
        data = response.json()
        recommendation = data['tracks'][0]['name']
        return recommendation
