import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] + ':' + os.environ['DB_PASSWORD'] + '@' + os.environ['DB_HOST'] + ":3306/" + os.environ['DB_DATABASE']

def get_config():
    return Config