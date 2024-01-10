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
    
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if file.filename.lower().rsplit('.', 1)[1] not in allowed_extensions:
        return jsonify({'error': 'Invalid file extension. Please upload a PNG, JPG, or JPEG image.'}), 400

    dominant_emotion = detect_emotion(file)

    if dominant_emotion == 400:
        return jsonify({'bad_request': 'Image cannot be analysed'}), 400

    music_genre = recommended_genres(dominant_emotion)
    recommended_songs = retrieve_songs(music_genre)

    return jsonify(recommended_songs)
