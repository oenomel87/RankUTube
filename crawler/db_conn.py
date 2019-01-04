from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

_engine = None
_Base = None

def engine():
    global _engine
    DB = config.DB
    if _engine is None:
        _path = 'mysql+pymysql://' + DB['USER'] + ':' + DB['PASSWORD']
        _path += '@localhost:' + str(DB['PORT']) + '/' + DB['DB_NAME']
        _path + '?charset=utf8mb4'
        _engine = create_engine(_path, echo=True)
    return _engine

def Base():
    global _Base
    if _Base is None:
        _Base = declarative_base()
    return _Base

def session():
    Session = sessionmaker(bind=engine())
    return Session()