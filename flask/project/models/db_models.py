
from project import db
from flask_sqlalchemy import SQLAlchemy


class StockListEntry(db.Model):

    market = db.Column(db.String(16), primary_key=True)
    ticker = db.Column(db.String(16), primary_key=True)

    def __init__(self, market, ticker):
        self.market = market
        self.ticker = ticker

    def __repr__(self):
        return '<Stock List Entry Object %s:%s>' % (self.market, self.ticker)
