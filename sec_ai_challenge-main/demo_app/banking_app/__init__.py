from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Import routes to register them with the app
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app