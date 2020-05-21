from flask import Flask
from feature1.core import api_task1

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    # from app import api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(api_task1, url_prefix = '/task1')
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)