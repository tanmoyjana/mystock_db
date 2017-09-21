from sqlalchemy import Column, Integer, Float, Date, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Company(Base):
    """class company"""
    __tablename__ = 'company'
    id = Column(Integer, Sequence('company_sequence_id'), primary_key=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    code = Column(String(16), nullable=False, unique=True, index=True)

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return "Company(name={self.name}, code={self.code})".format(self=self)

class Exchange(Base):
    """class exchange"""
    __tablename__ = 'exchange'
    id = Column(Integer, Sequence('exchange_sequence_id'), primary_key=True)
    name = Column(String(80), nullable=False)
    code = Column(String(8), unique=True, nullable=False, index=True)
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return "Exchange(name={self.name}, code={self.code})".format(self=self)

class Stock(Base):
    """
    company and exchange's stock
    """
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    code = Column(String(16), unique=True, nullable=False, index=True)
    company = relationship('Company', backref='company_stock', 
    cascade="all, delete-orphan", single_parent=True)
    exchange = relationship('Exchange',backref='exchange_stock', 
    cascade="all, delete-orphan", single_parent=True)
    def __init__(self, code):
        self.code = code
    def __repr__(self):
        return "Stock(code={self.code})".format(self=self)

class Price(Base):
    """stock price"""
    __tablename__ = 'price'
    date = Column(Date, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key=True)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    wap = Column(Float, nullable=False)
    last = Column(Float, nullable=False)
    volume = Column(Integer)
    turnover = Column(Float)
    stock = relationship('Stock', backref=backref('stock_price', order_by=date))

    def __init__(self, open, high, low, close, wap, last, volume, turnover):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.last = last
        self.wap = wap
        self.volume = volume
        self.turnover = turnover
    def __repr__(self):
        return "Price(open={self.open}, "\
        "high={self.high}, "\
        "low={self.low}, "\
        "close={self.close}, "\
        "last={self.last}, "\
        "wap={self.wap}, "\
        "volume={self.volume}"\
        "turnover={self.turnover})".format(self=self)
