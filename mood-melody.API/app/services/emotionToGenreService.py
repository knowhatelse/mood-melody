def getGenreFromEmotion(emotion):
    if emotion == "angry":
        return "rock"
    elif emotion == "disgust":
        return "rock"
    elif emotion == "fear":
        return "rock"
    elif emotion == "happy":
        return ["pop", "hip hop", "raggae", "country"]
    elif emotion == "sad":
        return ["jazz", "blues"]
    elif emotion == "surprise":
        return ["hip hop", "pop"]
    else:
        return ["pop", "country", "blues", "jazz", "raggae", "rock", "hip hop"]