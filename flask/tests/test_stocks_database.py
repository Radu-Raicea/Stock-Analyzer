
import unittest
from tests.base_database_test import BaseTestCase
from project.services.stocks import add_stock, get_stocks_from_google, get_stocks_from_db, object_to_dict, remove_stock
from project.models.db_models import StockListEntry


class TestStocksDatabase(BaseTestCase):

    def test_add_stock_successful(self):
        with self.client:
            add_stock('NASDAQ', 'AAPL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPL').first()
            self.assertTrue(stock)
            self.assertEqual(str(stock), '<Stock List Entry Object NASDAQ:AAPL>')

    def test_add_stock_fail(self):
        with self.client:
            stock = add_stock('NASDAQ', 'AAPLLL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPLLL').first()
            self.assertFalse(stock)

    def test_get_stocks_from_google(self):
        with self.client:
            stocks = get_stocks_from_google()
            self.assertEqual(stocks, [])

            add_stock('NASDAQ', 'AAPL')
            stocks = get_stocks_from_google()
            self.assertEqual(stocks[0]['market'], 'NASDAQ')
            self.assertEqual(stocks[0]['ticker'], 'AAPL')
            self.assertNotEqual(stocks[0]['price'], 'N/A')

    def test_get_stocks_from_db(self):
        with self.client:
            stocks = get_stocks_from_db()
            self.assertEqual(stocks, [])

            add_stock('NASDAQ', 'AAPL')
            stocks = get_stocks_from_db()
            self.assertEqual(stocks[0]['market'], 'NASDAQ')
            self.assertEqual(stocks[0]['ticker'], 'AAPL')
            self.assertEqual(stocks[0]['price'], 'N/A')

    def test_object_to_dictionary(self):
        with self.client:
            add_stock('NASDAQ', 'AAPL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPL').first()
            stock_dict = object_to_dict(stock)
            self.assertEqual(stock_dict['market'], 'NASDAQ')
            self.assertEqual(stock_dict['ticker'], 'AAPL')
            self.assertEqual(stock_dict['current_ratio'], 'N/A')

    def test_remove_stock_successful(self):
        with self.client:
            add_stock('NASDAQ', 'AAPL')
            remove_stock('NASDAQ', 'AAPL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPL').first()
            self.assertFalse(stock)

    def test_remove_stock_fail(self):
        with self.client:
            remove_stock('NASDAQ', 'AAPL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPL').first()
            self.assertFalse(stock)

if __name__ == '__main__':
    unittest.main()
