import os

class Config(object):
    ENV = os.environ['MODE']
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] + ':' + os.environ['DB_PASSWORD'] + '@' + os.environ['DB_HOST'] + ":3306/" + os.environ['DB_DATABASE']

class DEVConfig(Config):
    GRAPHIQL_ON = True

class PRODConfig(Config):
    GRAPHIQL_ON = False

def get_config():
    return DEVConfig if Config.ENV == "DEV" else PRODConfig