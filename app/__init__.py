from flask import Flask
from .route.routes import app_routes


def create_app():
    app = Flask(__name__)

    # Register the routes
    app.register_blueprint(app_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
