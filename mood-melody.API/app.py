from flask import Flask, jsonify
from app.validator.validator import file_validator

app = Flask(__name__)

@app.route('/index', methods=['POST'])
def index():
    validator_response = file_validator()

    if validator_response == 404:
        return jsonify({'response' : 'No file added'})
    
   
if __name__ == '__main__':
    app.run(debug=True)