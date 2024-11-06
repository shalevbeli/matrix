import os

FLASK_HOST = os.environ.get("FLASK_HOST","0.0.0.0")
FLASK_PORT = os.environ.get("FLASK_PORT","5000")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG","True")
MONGODB_HOST = os.environ.get("MONGODB_HOST","localhost")
MONGODB_PORT = os.environ.get("MONGODB_PORT",27017)
MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME","root")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD","example")
MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME","mydatabase")