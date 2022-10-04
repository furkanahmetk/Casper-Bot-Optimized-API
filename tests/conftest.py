import json
import functools
import os
import sys
import pytest
from flask import Flask
from src.config import *
# Set up the path to import from repository.
root = os.path.join(os.path.dirname(__file__))
package = os.path.join(root, '..')
sys.path.insert(0, os.path.abspath(package))

from src.app import create_app  # noqa

#Converts response to json
class TestResponseClass(Flask.response_class):
    @property
    def json(self):
        return json.loads(self.data)

#Set Flask response class to class stated above
Flask.response_class = TestResponseClass


def humanize_werkzeug_client(client_method):
    """Wraps a `werkzeug` client method (the client provided by `Flask`) to make
    it easier to use in tests.

    """
    @functools.wraps(client_method)
    def wrapper(url, **kwargs):
        # Always set the content type to `application/json`.
        kwargs.setdefault('headers', {}).update({
            'content-type': 'application/json'
        })

        # If data is present then make sure it is json encoded.
        if 'data' in kwargs:
            data = kwargs['data']
            if isinstance(data, dict):
                kwargs['data'] = json.dumps(data)

        kwargs['buffered'] = True

        return client_method(url, **kwargs)

    return wrapper

#Run flask app for testing purposes
@pytest.fixture(scope='session', autouse=True)
def app(request):
    
    app = create_app(TestingConfig)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def client(app, request):
    return app.test_client()

#A function that wraps Http method
@pytest.fixture(scope='function')
def get(client):
    return humanize_werkzeug_client(client.get)

    
