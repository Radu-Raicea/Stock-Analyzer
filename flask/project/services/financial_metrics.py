
from project.services.google_finance import GoogleFinance


class Stock(GoogleFinance):

    def __init__(self, market, ticker):
        super().__init__(market, ticker)

        self.inc = super().income_statement()
        self.bal = super().balance_sheet()
        self.cas = super().cash_flow()

    def generate_metrics(self):
        self.current_ratio = self._compute_current_ratio()
        self.quick_ratio = self._compute_quick_ratio()

    def _compute_current_ratio(self):
        if self.bal and self.bal[10][0] == 'Total Current Assets' and self.bal[23][0] == 'Total Current Liabilities':
            return self.bal[10][1] / self.bal[23][1]
        else:
            return None

    def _compute_quick_ratio(self):
        if self.bal and self.bal[10][0] == 'Total Current Assets' and self.bal[7][0] == 'Total Inventory' and self.bal[23][0] == 'Total Current Liabilities':
            return (self.bal[10][1] - self.bal[7][1]) / self.bal[23][1]
        else:
            return None
