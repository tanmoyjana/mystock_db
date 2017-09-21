from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import create_engine
from config import DBURL
from model import Base

engine = create_engine(DBURL)

if database_exists(engine.url):
    drop_database(engine.url)

create_database(engine.url)

Base.metadata.create_all(engine)
