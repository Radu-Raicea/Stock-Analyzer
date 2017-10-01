
import unittest
from tests.base_test import BaseTestCase
from project.services.financial_metrics import Stock


class TestFinancialMetrics(BaseTestCase):

    def test_current_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            stock.generate_metrics()
            self.assertTrue(stock.current_ratio)

    def test_current_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            stock.generate_metrics()
            self.assertFalse(stock.current_ratio)

    def test_quick_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            stock.generate_metrics()
            self.assertTrue(stock.quick_ratio)

    def test_quick_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            stock.generate_metrics()
            self.assertFalse(stock.quick_ratio)

if __name__ == '__main__':
    unittest.main()
