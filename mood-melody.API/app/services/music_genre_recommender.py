def recommended_genres(emotion):
    GENRE_MAP = {
        "angry": "rock",
        "disgust": "rock",
        "fear": "rock",
        "happy": ("pop", "hip hop", "reggae", "country"),
        "sad": ("jazz", "blues"),
        "surprise": ("hip hop", "pop"),
    }

    return GENRE_MAP.get(emotion, "pop")
