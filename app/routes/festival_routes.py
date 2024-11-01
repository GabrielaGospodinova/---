from flask import Blueprint, jsonify, request
from app.models import festivals, get_next_festival_id

bp = Blueprint('festivals', __name__)

@bp.route('/festivals', methods=['GET'])
def get_festivals():
    """
    Get all festivals
    ---
    responses:
      200:
        description: List of all festivals
    """
    return jsonify(festivals)

@bp.route('/festivals/<int:id>', methods=['GET'])
def get_festival(id):
    """
    Get a specific festival
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Festival details
      404:
        description: Festival not found
    """
    festival = next((f for f in festivals if f['id'] == id), None)
    if festival is None:
        return jsonify({'error': 'Festival not found'}), 404
    return jsonify(festival)

@bp.route('/festivals', methods=['POST'])
def create_festival():
    """
    Create a new festival
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            start_date:
              type: string
            end_date:
              type: string
            location:
              type: string
    responses:
      201:
        description: Festival created
    """
    data = request.get_json()
    festival = {
        'id': get_next_festival_id(),
        'name': data['name'],
        'start_date': data['start_date'],
        'end_date': data['end_date'],
        'location': data['location']
    }
    festivals.append(festival)
    return jsonify(festival), 201

@bp.route('/festivals/<int:id>', methods=['PUT'])
def update_festival(id):
    """
    Update a festival
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            start_date:
              type: string
            end_date:
              type: string
            location:
              type: string
    responses:
      200:
        description: Festival updated
      404:
        description: Festival not found
    """
    festival = next((f for f in festivals if f['id'] == id), None)
    if festival is None:
        return jsonify({'error': 'Festival not found'}), 404
    
    data = request.get_json()
    festival.update(data)
    return jsonify(festival)

@bp.route('/festivals/<int:id>', methods=['DELETE'])
def delete_festival(id):
    """
    Delete a festival
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Festival deleted
      404:
        description: Festival not found
    """
    festival = next((f for f in festivals if f['id'] == id), None)
    if festival is None:
        return jsonify({'error': 'Festival not found'}), 404
    
    festivals.remove(festival)
    return '', 204 