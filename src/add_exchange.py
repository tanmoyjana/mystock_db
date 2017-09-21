from sys import argv
import test_model
from model import Exchange
from config import DBURL
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


script, filename = argv

engine = create_engine(DBURL)
Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv(filename, sep=" ", header=0, names=['code', 'name'])


for i in range(0, len(data)):
    code = data['code'][i].strip(',')
    name = data['name'][i]
    session.add(Exchange(name, code))

session.commit()