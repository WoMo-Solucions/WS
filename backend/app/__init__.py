from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET"] = os.getenv("JWT_SECRET", "dev_secret")
    origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()]
    CORS(app, resources={r"/*": {"origins": origins}}, supports_credentials=True)

    from .core.auth import bp as auth_bp
    from .core.dashboard import bp as dash_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dash_bp, url_prefix="/")

    return app
