import csv
import random
from os.path import join, dirname

class SongService:
    def __init__(self):
        self.csv_path = join(dirname(__file__), '../dataset/song-data.csv')
        
    def get_songs(self, genres=None):
        with open(self.csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            songs = [row for row in reader]
        
        if genres:
            if isinstance(genres, str):
                genres = [genres]
            songs = [song for song in songs if song['Genre'] in genres]
        
        if len(songs) < 10:
            return None
        
        random_songs = random.sample(songs, 10)
        
        result = [
            {'Artist': song['ArtistName'], 'Track': song['TrackName'], 'ReleaseDate': song['RelaseDate'], 'Genre' : song['Genre']}
            for song in random_songs
        ]

        return result
