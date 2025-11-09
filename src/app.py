"""
Main Flask application with modular route handlers
"""
from flask import Flask
from .routes import main_routes, api_routes, error_handlers

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(api_routes.bp)
    
    # Register error handlers
    error_handlers.register_error_handlers(app)
    
    # Security headers middleware
    @app.after_request
    def add_security_headers(response):
        """Add security headers to all responses"""
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    
    return app

# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
