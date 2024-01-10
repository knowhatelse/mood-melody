import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), '../datasets/songs.csv')
songs_df = pd.read_csv(csv_file_path, delimiter=';')

def retrieve_songs(genres):
    global songs_df

    if genres:
        genres = set(genres) if isinstance(genres, (str, tuple)) else set(genres)
        df = songs_df[songs_df['Genre'].isin(genres)]
    else:
        df = songs_df 

    if len(df) < 10:
        return None

    random_songs = df.sample(n=10)

    return [
        {'Artist': song['ArtistName'], 'Track': song['TrackName'], 'ReleaseDate': song['RelaseDate'], 'Genre': song['Genre']}
        for song in random_songs.to_dict('records')
    ]
