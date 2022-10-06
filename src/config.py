"""Flask configuration."""
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

class Config:
    """Base config."""
    BASE_URL = 'https://event-store-api-clarity-mainnet.make.services'
    APISPEC_SPEC= APISpec(
        title='Casper Bot Optimized API',
        version='v0.1.0',
        openapi_version = '2.0',
        plugins=[MarshmallowPlugin()],
    )
    APISPEC_SWAGGER_URL= '/swagger/'

class ProdConfig(Config):
    """config for production environment."""
    DEBUG = True
    TESTING = False
    MONGO_URI = 'mongodb://localhost:27017'
    DB_NAME = 'bot_optimized'


class TestingConfig(Config):
    """config for testing environment."""
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017'
    DB_NAME = 'bot_opt_test'

