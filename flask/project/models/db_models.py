
from project import db
from flask_sqlalchemy import SQLAlchemy


class StockListEntry(db.Model):

    market = db.Column(db.String(16), primary_key=True)
    ticker = db.Column(db.String(16), primary_key=True)
    price = db.Column(db.Float)
    current_ratio = db.Column(db.Float)
    quick_ratio = db.Column(db.Float)
    return_on_equity = db.Column(db.Float)
    debt_equity_ratio = db.Column(db.Float)
    net_profit_margin = db.Column(db.Float)
    free_cash_flow = db.Column(db.Float)
    price_to_earnings_ratio = db.Column(db.Float)

    def __init__(self, market, ticker):
        self.market = market
        self.ticker = ticker

    def __repr__(self):
        return '<Stock List Entry Object %s:%s>' % (self.market, self.ticker)
