from flask import Flask, jsonify, request
from app.validator.validator import file_validator
from app.services.emotionDetectionService import detectEmotion
from app.services.emotionToGenreService import getGenreFromEmotion
from app.services.songService import SongService

app = Flask(__name__)

@app.route('/index', methods=['POST'])
def index():
    validator_response = file_validator()

    if validator_response == 404:
        return jsonify({'response' : 'No file added'})
    
    emotion_result = detectEmotion(validator_response)

    if emotion_result == 400:
        return jsonify({'error' : 'Problem with analyzing the image...'})
    
    genre = getGenreFromEmotion(emotion_result)

    song_service = SongService()
    songs = song_service.get_songs(genre)
    
    return jsonify({'songs' : songs})

if __name__ == '__main__':
    app.run(debug=True)