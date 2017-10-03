
from flask_sqlalchemy import inspect
from project.models.db_models import StockListEntry
from project.services.financial_metrics import Stock
from project import db, logger
import traceback


def add_stock(market, ticker):
    try:
        stock = Stock(market, ticker)
        stock.generate_metrics()
        if stock.data and stock.data['price']:
            stock_list_entry = StockListEntry(market.upper(), ticker.upper())
            db.session.add(stock_list_entry)
            db.session.commit()
        return stock
    except Exception as e:
        logger.error(traceback.format_exc())


def get_stocks_from_google():
    try:
        stocks = []
        stock_list_entries = StockListEntry.query.all()

        for stock_list_entry in stock_list_entries:
            stock = Stock(stock_list_entry.market, stock_list_entry.ticker)
            stock.generate_metrics()

            for key, value in stock.data.items():
                setattr(stock_list_entry, key, value)

            db.session.commit()
            stocks.append(object_to_dict(stock_list_entry))

        return stocks
    except Exception as e:
        logger.error(traceback.format_exc())


def get_stocks_from_db():
    try:
        stocks = []
        stock_list_entries = StockListEntry.query.all()

        for stock_list_entry in stock_list_entries:
            stocks.append(object_to_dict(stock_list_entry))

        return stocks
    except Exception as e:
        logger.error(traceback.format_exc())


def object_to_dict(obj):
    object_dict = {}

    for col in inspect(obj).mapper.column_attrs:
        value = getattr(obj, col.key)
        if value:
            object_dict[col.key] = value
        else:
            object_dict[col.key] = 'N/A'

    return object_dict


def remove_stock(market, ticker):
    try:
        stock_list_entry = StockListEntry.query.filter_by(market=market, ticker=ticker).first()
        if stock_list_entry:
            db.session.delete(stock_list_entry)
            db.session.commit()
    except Exception as e:
        logger.error(traceback.format_exc())
