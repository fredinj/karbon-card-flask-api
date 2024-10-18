import os

class Config:
    # Basic Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Replace with a secure key in production
    DEBUG = os.getenv('DEBUG', True)

    # Database settings (example configuration)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///karboncard.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False