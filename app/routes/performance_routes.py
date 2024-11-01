from flask import Blueprint, jsonify, request
from app.models import (
    performances, get_next_performance_id,
    festivals, artists, stages
)

bp = Blueprint('performances', __name__)

@bp.route('/performances', methods=['GET'])
def get_performances():
    """
    Get all performances
    ---
    responses:
      200:
        description: List of all performances
    """
    return jsonify(performances)

@bp.route('/performances/<int:id>', methods=['GET'])
def get_performance(id):
    """
    Get a specific performance
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Performance details
      404:
        description: Performance not found
    """
    performance = next((p for p in performances if p['id'] == id), None)
    if performance is None:
        return jsonify({'error': 'Performance not found'}), 404
    return jsonify(performance)

@bp.route('/performances', methods=['POST'])
def create_performance():
    """
    Create a new performance
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            festival_id:
              type: integer
            artist_id:
              type: integer
            stage_id:
              type: integer
            start_time:
              type: string
              format: date-time
            end_time:
              type: string
              format: date-time
    responses:
      201:
        description: Performance created
      400:
        description: Invalid festival, artist, or stage ID
    """
    data = request.get_json()
    
    # Validate that festival, artist, and stage exist
    festival = next((f for f in festivals if f['id'] == data['festival_id']), None)
    artist = next((a for a in artists if a['id'] == data['artist_id']), None)
    stage = next((s for s in stages if s['id'] == data['stage_id']), None)
    
    if not festival:
        return jsonify({'error': 'Festival not found'}), 400
    if not artist:
        return jsonify({'error': 'Artist not found'}), 400
    if not stage:
        return jsonify({'error': 'Stage not found'}), 400
    
    performance = {
        'id': get_next_performance_id(),
        'festival_id': data['festival_id'],
        'artist_id': data['artist_id'],
        'stage_id': data['stage_id'],
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }
    performances.append(performance)
    return jsonify(performance), 201

@bp.route('/performances/<int:id>', methods=['PUT'])
def update_performance(id):
    """
    Update a performance
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
            festival_id:
              type: integer
            artist_id:
              type: integer
            stage_id:
              type: integer
            start_time:
              type: string
              format: date-time
            end_time:
              type: string
              format: date-time
    responses:
      200:
        description: Performance updated
      404:
        description: Performance not found
      400:
        description: Invalid festival, artist, or stage ID
    """
    performance = next((p for p in performances if p['id'] == id), None)
    if performance is None:
        return jsonify({'error': 'Performance not found'}), 404
    
    data = request.get_json()
    
    # Validate references if they're being updated
    if 'festival_id' in data:
        festival = next((f for f in festivals if f['id'] == data['festival_id']), None)
        if not festival:
            return jsonify({'error': 'Festival not found'}), 400
            
    if 'artist_id' in data:
        artist = next((a for a in artists if a['id'] == data['artist_id']), None)
        if not artist:
            return jsonify({'error': 'Artist not found'}), 400
            
    if 'stage_id' in data:
        stage = next((s for s in stages if s['id'] == data['stage_id']), None)
        if not stage:
            return jsonify({'error': 'Stage not found'}), 400 