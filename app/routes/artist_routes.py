from flask import Blueprint, jsonify, request
from app.models import artists, get_next_artist_id

bp = Blueprint('artists', __name__)

@bp.route('/artists', methods=['GET'])
def get_artists():
    """
    Get all artists
    ---
    responses:
      200:
        description: List of all artists
    """
    return jsonify(artists)

@bp.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    """
    Get a specific artist
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Artist details
      404:
        description: Artist not found
    """
    artist = next((a for a in artists if a['id'] == id), None)
    if artist is None:
        return jsonify({'error': 'Artist not found'}), 404
    return jsonify(artist)

@bp.route('/artists', methods=['POST'])
def create_artist():
    """
    Create a new artist
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
            genre:
              type: string
            bio:
              type: string
    responses:
      201:
        description: Artist created
    """
    data = request.get_json()
    artist = {
        'id': get_next_artist_id(),
        'name': data['name'],
        'genre': data.get('genre', ''),
        'bio': data.get('bio', '')
    }
    artists.append(artist)
    return jsonify(artist), 201

@bp.route('/artists/<int:id>', methods=['PUT'])
def update_artist(id):
    """
    Update an artist
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
            genre:
              type: string
            bio:
              type: string
    responses:
      200:
        description: Artist updated
      404:
        description: Artist not found
    """
    artist = next((a for a in artists if a['id'] == id), None)
    if artist is None:
        return jsonify({'error': 'Artist not found'}), 404
    
    data = request.get_json()
    artist.update(data)
    return jsonify(artist)

@bp.route('/artists/<int:id>', methods=['DELETE'])
def delete_artist(id):
    """
    Delete an artist
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Artist deleted
      404:
        description: Artist not found
    """
    artist = next((a for a in artists if a['id'] == id), None)
    if artist is None:
        return jsonify({'error': 'Artist not found'}), 404
    
    artists.remove(artist)
    return '', 204