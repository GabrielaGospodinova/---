# Music Festival API
A Flask-based REST API for managing music festivals, artists, stages, and performances.

## Project Structure

festival-api/
├── app/
│ ├── init.py # App initialization and configuration
│ ├── models/
│ │ └── init.py # Data models and storage
│ └── routes/
│ ├── artist_routes.py
│ ├── festival_routes.py
│ ├── stage_routes.py
│ └── performance_routes.py
├── requirements.txt
└── run.py


## Installation

1. Clone the repository
2. Create a virtual environment(make sure python is installed beforehand):
```
python -m venv venv
```
3. Activate the virtual environment:
```
source venv/bin/activate
```
4. Install the dependencies:
```
pip install -r requirements.txt
```
5. Run the application:
```
python run.py
```


# API Documentation

Access the Swagger UI documentation at: `http://127.0.0.1:5000/docs/`

### Available Endpoints

#### Artists
- GET /artists - List all artists
- GET /artists/{id} - Get specific artist
- POST /artists - Create new artist
- PUT /artists/{id} - Update artist
- DELETE /artists/{id} - Delete artist

#### Festivals
- GET /festivals - List all festivals
- GET /festivals/{id} - Get specific festival
- POST /festivals - Create new festival
- PUT /festivals/{id} - Update festival
- DELETE /festivals/{id} - Delete festival

#### Stages
- GET /stages - List all stages
- GET /stages/{id} - Get specific stage
- POST /stages - Create new stage
- PUT /stages/{id} - Update stage
- DELETE /stages/{id} - Delete stage

#### Performances
- GET /performances - List all performances
- GET /performances/{id} - Get specific performance
- POST /performances - Create new performance
- PUT /performances/{id} - Update performance
- DELETE /performances/{id} - Delete performance

## Data Storage

The application uses in-memory storage with the following structures:
- Lists for storing entities (artists, festivals, stages, performances)
- Auto-incrementing ID counters for each entity type

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 201: Created
- 204: Deleted
- 400: Bad Request
- 404: Not Found
