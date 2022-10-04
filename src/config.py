"""Flask configuration."""


class Config:
    """Base config."""
    BASE_URL = 'https://event-store-api-clarity-mainnet.make.services'

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

