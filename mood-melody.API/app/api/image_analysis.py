from flask import Blueprint, request, jsonify
from app.services.image_analysis_service import detect_emotion
from app.services.music_genre_recommender import recommended_genres
from app.services.song_retriever import retrieve_songs

image_analysis_bp = Blueprint('image_analysis', __name__)

@image_analysis_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    dominant_emotion = detect_emotion(file)
    music_genre = recommended_genres(dominant_emotion)
    recommended_songs = retrieve_songs(music_genre)

    return jsonify(recommended_songs)
