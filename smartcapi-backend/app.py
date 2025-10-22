import os
from flask import Flask
from app import db

def create_app(config_overrides=None):
    app = Flask(__name__)
    database_url = os.getenv("DATABASE_URL", "sqlite:///smartcapi.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config_overrides:
        app.config.update(config_overrides)

    db.init_app(app)

    # Import models to register with SQLAlchemy metadata
    with app.app_context():
        # Import here to avoid circular import at module import time
        import app.models  # noqa: F401

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
