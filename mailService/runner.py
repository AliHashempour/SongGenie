import time

from dbHelper.mongoDB import select_ready_records, update_status
from mailService.mailgunWorker import send_simple_message
from spotifyHelper.spotifyWorker import SpotifyWorker

if __name__ == '__main__':
    spotify_worker = SpotifyWorker()
    while True:
        ready_records = select_ready_records()
        for record in ready_records:
            recommendation = spotify_worker.send_recommend_request(song_id=record["songId"])
            send_simple_message(email=record["email"], text=recommendation)
            update_status(record['_id'], "Done")
        time.sleep(20)
