
from project.services.google_finance import GoogleFinance


def get_google_finance_stock(market, ticker):
    return GoogleFinance(market, ticker)


def get_current_ratio(market, ticker):

    report = get_google_finance_stock(market, ticker).balance_sheet()

    if report and report[10][0] == 'Total Current Assets' and report[23][0] == 'Total Current Liabilities':
        return report[10][1] / report[23][1]
    else:
        return None


def get_quick_ratio(market, ticker):

    report = get_google_finance_stock(market, ticker).balance_sheet()

    if report and report[10][0] == 'Total Current Assets' and report[7][0] == 'Total Inventory' and report[23][0] == 'Total Current Liabilities':
        return (report[10][1] - report[7][1]) / report[23][1]
    else:
        return None
