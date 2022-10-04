from flask import Blueprint, jsonify
from marshmallow import ValidationError
errors = Blueprint('errors', __name__)

class APIError(Exception):
    def __init__(self, code, description):
        self.code = code
        self.description = description



@errors.app_errorhandler(ValidationError)
def handle_error(error):
    """Return custom JSON when ValidationError or its children are raised"""
    message = [str(x[0]) for x in list(error.messages.values())]
    status_code = 400
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    return jsonify(response), status_code

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    """Return custom JSON when non spesific or its children are raised"""
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.',
            'error': str(error)
        }
    }
    return jsonify(response), status_code

@errors.app_errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'APIError',
            'message': err.description
        }
    }
    return jsonify(response), err.code

