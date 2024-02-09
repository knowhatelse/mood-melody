import pandas as pd
import os

def retrieve_songs(dataset_location):
    if not os.path.isfile(dataset_location):
        print(f"Error: File not found at {dataset_location}")
        return None

    try:
        songs_df = pd.read_csv(dataset_location, delimiter=";", encoding="latin-1")
    except FileNotFoundError:
        print(f"Error: File not found at {dataset_location}")
        return None

    random_songs = songs_df.sample(n=10)

    return [
        {'Artist': song['artist_name'], 'Track': song['track_name'],
         'ReleaseDate': song['release_date'], 'Genre': song['genre']}
        for song in random_songs.to_dict('records')
    ]