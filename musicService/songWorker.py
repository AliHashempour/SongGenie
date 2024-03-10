from dbHelper.mongoDB import update_songId
from shazamHelper.shazamWorker import ShazamWorker
from spotifyHelper.spotifyWorker import SpotifyWorker
from storageHelper.s3 import download_object


class SongWorker:
    def __init__(self, message):
        self.msg = message

    def process_message(self):
        file = download_object(self.msg)
        shazam_helper = ShazamWorker(file_name=file)
        song_name, artist = shazam_helper.send_request_to_shazam()
        concatenated_name = f'{song_name} {artist} '
        spotify_worker = SpotifyWorker()
        song_id = spotify_worker.send_search_request(search_song=concatenated_name)
        record_id = file.split(".")[0]
        update_songId(_id=record_id, song_id=song_id)
