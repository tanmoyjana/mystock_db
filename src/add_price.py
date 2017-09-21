from sys import argv
from model import Price
from config import DBURL
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

script, filename = argv

engine = create_engine(DBURL)

Session = sessionmaker(bind = engine)

session = Session()

data = pd.read_csv(filename, sep=" ", header=0, names=['code', 'name'])


for i in range(0,len(data)):
    open = data['open'][i]
    high = data['high'][i]
    low = data['low'][i]
    close = data['close']
    wap = data['wap']
    last = data['last']
    volume = data['volume']
    session.add(Price(open, high, low, close, wap, last, volume))

session.commit()
