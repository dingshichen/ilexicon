from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

def register_blueprints(app):
    from . import word
    app.register_blueprint(api)