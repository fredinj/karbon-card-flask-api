from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/api/items', methods=['GET'])
def get_items():
    # Example response
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return jsonify(items)

@api.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()  # Get JSON data from the request
    new_item = {"id": 3, "name": data['name']}  # Example item creation
    return jsonify(new_item), 201  # Return created item with 201 status