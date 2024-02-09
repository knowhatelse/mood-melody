from flask import Flask
from app.api.image_analysis import image_analysis_bp
from app.api.song_retriever import song_finder_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_analysis_bp)
    app.register_blueprint(song_finder_bp)
    return app
