"""
Error handlers
"""
from flask import render_template

def register_error_handlers(app):
    """Register error handlers with the Flask app"""
    
    @app.errorhandler(404)
    def page_not_found(e):
        """Custom 404 error page"""
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        """Custom 500 error page"""
        return render_template('500.html'), 500
