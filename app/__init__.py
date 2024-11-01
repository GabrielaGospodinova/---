from flask import Flask
from flasgger import Swagger

# Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
def create_app():
    app = Flask(__name__)
    Swagger(app, config=swagger_config)
    
    # Import all blueprints
    from app.routes.festival_routes import bp as festival_bp
    from app.routes.artist_routes import bp as artist_bp
    from app.routes.stage_routes import bp as stage_bp
    from app.routes.performance_routes import bp as performance_bp

    # Register all app blueprints to setup the routes
    app.register_blueprint(festival_bp)
    app.register_blueprint(artist_bp)
    app.register_blueprint(stage_bp)
    app.register_blueprint(performance_bp)
    
    return app