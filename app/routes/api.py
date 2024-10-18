from flask import Blueprint, jsonify, request
import json
from karbon import model


api = Blueprint('api', __name__)
  
@api.route('/upload-data', methods=['POST'])
def upload_json():
    try:
        # Check if a file is part of the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']

        # Check if the file has a name and is a JSON file
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if not file.filename.endswith('.json'):
            return jsonify({"error": "File must be a JSON file"}), 400

        # Load the JSON data from the file
        data = json.load(file)

        flags = model.probe_model_5l_profit(data['data'])

        return jsonify(flags), 200  
    except Exception as e:
        return jsonify({"error": str(e)}), 500
