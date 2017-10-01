
import unittest
from tests.base_test import BaseTestCase
from project.services.financial_metrics import get_current_ratio, get_quick_ratio


class TestFinancialMetrics(BaseTestCase):

    def test_current_ratio_success(self):
        with self.client:
            current_ratio = get_current_ratio('NASDAQ', 'TSLA')
            self.assertTrue(current_ratio)

    def test_current_ratio_fail(self):
        with self.client:
            current_ratio = get_current_ratio('NASDAQ', 'TSLAA')
            self.assertFalse(current_ratio)

    def test_quick_ratio_success(self):
        with self.client:
            quick_ratio = get_quick_ratio('NASDAQ', 'TSLA')
            self.assertTrue(quick_ratio)

    def test_quick_ratio_fail(self):
        with self.client:
            quick_ratio = get_quick_ratio('NASDAQ', 'TSLAA')
            self.assertFalse(quick_ratio)


if __name__ == '__main__':
    unittest.main()
