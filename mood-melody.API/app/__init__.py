from flask import Flask
from app.api.image_analysis import image_analysis_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_analysis_bp)
    return app
