#from sys import argv
from model import Company, Stock
from config import DBURL
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy
#script, filename = argv
#filename = 'data/comp.csv'
f1 = 'data/bse-stock-list.csv'
f2 = 'data/nse-stock-list.csv'

engine = create_engine(DBURL)
Session = sessionmaker(bind = engine)
session = Session()

data1 = pd.read_csv(f1, sep=",", header=0)
data2 = pd.read_csv(f2, sep=",", header=0)
data = pd.merge(data1, data2, how='inner', on=['Co_Name'])
data_index = []
for i in range(0,len(data)):
    if data.duplicated('Co_Name')[i] == False:
        code = data['NSE_Symbol'][i]
        name = data['Co_Name'][i]
        session.add(Company(name, code))
    else:
        data_index.append(i)
session.commit()
