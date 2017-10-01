
from project.models.db_models import StockListEntry
from project.services.financial_metrics import Stock
from project import db, logger
import traceback


def add_stock(market, ticker):
    try:
        stock = Stock(market, ticker)
        stock.generate_metrics()
        if stock.data and stock.data['price']:
            stock_list_entry = StockListEntry(market, ticker)
            db.session.add(stock_list_entry)
            db.session.commit()
        return stock
    except Exception as e:
        logger.error(traceback.format_exc())


def get_stock_metrics():
    try:
        stocks = []
        stock_list_entries = StockListEntry.query.all()

        for stock_list_entry in stock_list_entries:
            stock = Stock(stock_list_entry.market, stock_list_entry.ticker)
            stock.generate_metrics()
            stocks.append(stock)

        return stocks
    except Exception as e:
        logger.error(traceback.format_exc())


def remove_stock(market, ticker):
    try:
        stock_list_entry = StockListEntry.query.filter_by(market=market, ticker=ticker).first()
        if stock_list_entry:
            db.session.delete(stock_list_entry)
            db.session.commit()
    except Exception as e:
        logger.error(traceback.format_exc())
