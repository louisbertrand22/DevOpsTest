"""
API endpoints
"""
from flask import Blueprint, jsonify
import datetime
import os

bp = Blueprint('api', __name__, url_prefix='/api')

# Application metadata
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
START_TIME = datetime.datetime.now()

@bp.route("/health")
def health_check():
    """Health check endpoint for Kubernetes liveness/readiness probes"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

@bp.route("/info")
def app_info():
    """Application information endpoint"""
    uptime = datetime.datetime.now() - START_TIME
    return jsonify({
        "application": "DevOps Documentation Hub",
        "version": APP_VERSION,
        "author": "Louis BERTRAND",
        "uptime_seconds": int(uptime.total_seconds()),
        "start_time": START_TIME.isoformat(),
        "routes": {
            "documentation": "/",
            "deployment_guide": "/deployment",
            "contribute": "/contribute",
            "health": "/api/health",
            "info": "/api/info"
        }
    }), 200
