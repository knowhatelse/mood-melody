def recommended_genres(emotion):
    GENRE_MAP = {
        "angry": ("rock", "rock"),
        "disgust": ("rock", "rock"),
        "fear": ("rock", "rock"),
        "happy": ("pop", "hip hop", "reggae", "country"),
        "sad": ("jazz", "blues"),
        "surprise": ("hip hop", "pop"),
        "neutral" : ("rock", "hip hop", "blues", "jazz", "reggae", "country", "pop")
    }

    return GENRE_MAP.get(emotion)
