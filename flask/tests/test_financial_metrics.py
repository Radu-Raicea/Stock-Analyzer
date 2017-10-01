
import unittest
from tests.base_test import BaseTestCase
from project.services.financial_metrics import Stock


class TestFinancialMetrics(BaseTestCase):

    def test_generate_metrics(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            stock.generate_metrics()
            self.assertTrue(stock.current_ratio)
            self.assertTrue(stock.quick_ratio)
            self.assertTrue(stock.return_on_equity)
            self.assertTrue(stock.debt_equity_ratio)
            self.assertTrue(stock.net_profit_margin)

    def test_current_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_current_ratio())

    def test_current_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_current_ratio())

    def test_quick_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_quick_ratio())

    def test_quick_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_quick_ratio())

    def test_shareholders_equity_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_shareholders_equity())

    def test_shareholders_equity_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_shareholders_equity())

    def test_return_on_equity_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_return_on_equity())

    def test_return_on_equity_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_return_on_equity())

    def test_debt_equity_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_debt_equity_ratio())

    def test_debt_equity_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_debt_equity_ratio())

    def test_net_profit_margin_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_net_profit_margin())

    def test_net_profit_margin_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_net_profit_margin())

if __name__ == '__main__':
    unittest.main()
