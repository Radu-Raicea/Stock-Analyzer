
from project.services.google_finance import GoogleFinance


def get_current_ratio(market, ticker):
    google_finance = GoogleFinance(market, ticker)
    report = google_finance.balance_sheet()
    if report[10][0] == 'Total Current Assets' and report[23][0] == 'Total Current Liabilities':
        return report[10][1] / report[23][1]
    else:
        return None
