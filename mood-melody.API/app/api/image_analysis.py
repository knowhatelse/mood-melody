from flask import Blueprint, request, jsonify
from app.services.image_analysis_service import detect_emotion

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
     
    return jsonify({'emotion': dominant_emotion}), 200
