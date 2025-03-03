from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        # Keeping here in case I need a config.
    )

    # Register blueprints or routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app