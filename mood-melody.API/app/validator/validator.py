from flask import request

def file_validator():
    if 'file' not in request.files:
        return 404
    
    file = request.files['file']

    if file.filename == '':
        return 404
    
    return file