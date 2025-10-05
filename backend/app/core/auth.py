from flask import Blueprint, jsonify

bp = Blueprint("auth", __name__)

@bp.get("/me")
def me():
    return jsonify({"user": "admin@example.com", "roles": ["admin"], "source": "WS-Core"})
