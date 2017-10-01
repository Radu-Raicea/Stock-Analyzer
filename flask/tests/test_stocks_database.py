
import unittest
from tests.base_database_test import BaseTestCase
from project.services.stocks import add_stock, get_stock_metrics, remove_stock
from project.models.db_models import StockListEntry


class TestStocksDatabase(BaseTestCase):

    def test_add_stock_successful(self):
        with self.client:
            add_stock('NASDAQ', 'AAPL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPL').first()
            self.assertTrue(stock)

    def test_add_stock_fail(self):
        with self.client:
            add_stock('NASDAQ', 'AAPLLL')
            stock = StockListEntry.query.filter_by(market='NASDAQ', ticker='AAPLLL').first()
            self.assertFalse(stock)

    def test_get_stock_metrics(self):
        with self.client:
            stocks = get_stock_metrics()
            self.assertEqual(stocks, [])

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
