from flask import Blueprint, jsonify

bp = Blueprint("dashboard", __name__)

@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "ws-backend"})
