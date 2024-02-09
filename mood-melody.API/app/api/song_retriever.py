from flask import Blueprint, request, jsonify
from app.services.dataset_finder_service import find_dataset
from app.services.song_retriever_service import retrieve_songs

song_finder_bp = Blueprint('song_finder', __name__)

@song_finder_bp.route('/find-songs', methods=['POST'])
def find_songs():
    request_data = request.json

    if 'emotion' not in request_data:
        return jsonify({'error': 'Missing emotion parameter'}), 400

    emotion = request_data['emotion']
    dataset_filepath = find_dataset(emotion)
    recommended_songs = retrieve_songs(dataset_filepath)

    return jsonify(recommended_songs)
