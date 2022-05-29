import os


SECRET_KEY = os.urandom(32)# Grabs the folder where the script runs.

basedir = os.path.abspath(os.path.dirname(__file__))# Enable debug mode.

DEBUG = True# Connect to the database

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Root123+@localhost/cynaxStore'# Turn off the Flask-SQLAlchemy event system and warning

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/myDbName"
SQLALCHEMY_TRACK_MODIFICATIONS = False
