from sys import argv
from model import Stock, Exchange, Company
from config import DBURL
import pandas as pd
from sqlalchemy.orm import sessionmaker, relation, backref
from sqlalchemy import create_engine
script, filename = argv
#filename = 'data/stock.csv'

engine = create_engine(DBURL)

Session = sessionmaker(bind = engine)

session = Session()

data = pd.read_csv(filename, sep=',', header=0)


for i in range(0,len(data)):
    code = data['key'][i]
    session.add(Stock(code))

session.commit()
