
import unittest
from tests.base_test import BaseTestCase
from project.services.financial_metrics import Stock


class TestFinancialMetrics(BaseTestCase):

    def test_generate_metrics(self):
        with self.client:
            stock = Stock('NASDAQ', 'AAPL')
            stock.generate_metrics()
            self.assertTrue(stock.data['price'])
            self.assertTrue(stock.data['current_ratio'])
            self.assertTrue(stock.data['quick_ratio'])
            self.assertTrue(stock.data['return_on_equity'])
            self.assertTrue(stock.data['debt_equity_ratio'])
            self.assertTrue(stock.data['net_profit_margin'])
            self.assertTrue(stock.data['free_cash_flow'])
            self.assertTrue(stock.data['price_to_earnings_ratio'])

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

    def test_free_cash_flow_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLA')
            self.assertTrue(stock._compute_free_cash_flow())

    def test_free_cash_flow_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._compute_free_cash_flow())

    def test_price_to_earnings_ratio_success(self):
        with self.client:
            stock = Stock('NASDAQ', 'AAPL')
            self.assertTrue(stock._get_price_to_earnings_ratio())

    def test_price_to_earnings_ratio_fail(self):
        with self.client:
            stock = Stock('NASDAQ', 'TSLAA')
            self.assertFalse(stock._get_price_to_earnings_ratio())

if __name__ == '__main__':
    unittest.main()
