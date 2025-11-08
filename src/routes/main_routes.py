"""
Main page routes
"""
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route("/")
def documentation():
    """Main documentation page"""
    return render_template('index.html')

@bp.route("/deployment")
def deployment():
    """Azure deployment guide page"""
    return render_template('deployment.html')

@bp.route("/contribute")
def contribute():
    """Contribution and contact page"""
    return render_template('contribute.html')
