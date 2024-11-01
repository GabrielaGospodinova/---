from flask import Blueprint, jsonify, request
from app.models import stages, get_next_stage_id

bp = Blueprint('stages', __name__)

@bp.route('/stages', methods=['GET'])
def get_stages():
    """
    Get all stages
    ---
    responses:
      200:
        description: List of all stages
    """
    return jsonify(stages)

@bp.route('/stages/<int:id>', methods=['GET'])
def get_stage(id):
    """
    Get a specific stage
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Stage details
      404:
        description: Stage not found
    """
    stage = next((s for s in stages if s['id'] == id), None)
    if stage is None:
        return jsonify({'error': 'Stage not found'}), 404
    return jsonify(stage)

@bp.route('/stages', methods=['POST'])
def create_stage():
    """
    Create a new stage
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
            capacity:
              type: integer
            location_description:
              type: string
    responses:
      201:
        description: Stage created
    """
    data = request.get_json()
    stage = {
        'id': get_next_stage_id(),
        'name': data['name'],
        'capacity': data.get('capacity', 0),
        'location_description': data.get('location_description', '')
    }
    stages.append(stage)
    return jsonify(stage), 201

@bp.route('/stages/<int:id>', methods=['PUT'])
def update_stage(id):
    """
    Update a stage
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
            capacity:
              type: integer
            location_description:
              type: string
    responses:
      200:
        description: Stage updated
      404:
        description: Stage not found
    """
    stage = next((s for s in stages if s['id'] == id), None)
    if stage is None:
        return jsonify({'error': 'Stage not found'}), 404
    
    data = request.get_json()
    stage.update(data)
    return jsonify(stage)

@bp.route('/stages/<int:id>', methods=['DELETE'])
def delete_stage(id):
    """
    Delete a stage
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Stage deleted
      404:
        description: Stage not found
    """
    stage = next((s for s in stages if s['id'] == id), None)
    if stage is None:
        return jsonify({'error': 'Stage not found'}), 404
    
    stages.remove(stage)
    return '', 204