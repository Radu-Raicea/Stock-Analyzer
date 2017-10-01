
import re
from decimal import Decimal
from datetime import date
from pyquery import PyQuery
import requests
import json

GOOGLE_FINANCE_REPORT_TYPES = {
    'inc': 'Income Statement',
    'bal': 'Balance Sheet',
    'cas': 'Cash Flow',
}

DATE = re.compile('.*(\d{4})-(\d{2})-(\d{2}).*')


class GoogleFinance(object):

    STOCK_URL = 'https://finance.google.com/finance?q={}%3A{}&output=json'
    FINANCIALS_URL = 'https://finance.google.com/finance?q={}%3A{}&fstype=ii'

    def __init__(self, market, ticker):
        self.market = market.upper()
        self.ticker = ticker.upper()
        self._stock_data = None
        self._financial = None

    @staticmethod
    def _parse_number(number_string):
        if number_string == '-':
            return None
        try:
            return Decimal(number_string.replace(',', ''))
        except Exception as e:
            pass
        return number_string

    @staticmethod
    def _parse_date(date_string):
        m = DATE.match(date_string)
        if m:
            return date(*[int(e) for e in m.groups()])
        return date_string

    def _get_from_google(self):
        return PyQuery(self.FINANCIALS_URL.format(self.market, self.ticker))

    def _get_stock_data(self):
        response = requests.get(self.STOCK_URL.format(self.market, self.ticker))
        try:
            data = json.loads(response.content[6:-2].decode('unicode_escape'))
            _stock_data = data
            stock_data = {}
            stock_data['price'] = self._parse_number(data['l'])
            stock_data['price_change'] = data['c']
            stock_data['percent_change'] = data['cp']
            stock_data['day_high'] = self._parse_number(data['hi'])
            stock_data['day_low'] = self._parse_number(data['lo'])
            stock_data['52_high'] = self._parse_number(data['hi52'])
            stock_data['52_low'] = self._parse_number(data['lo52'])
            stock_data['open'] = self._parse_number(data['op'])
            stock_data['volume'] = data['vo']
            stock_data['average_volume'] = data['avvo']
            stock_data['market_cap'] = data['mc']
            stock_data['price_to_earnings'] = self._parse_number(data['pe'])
            stock_data['dividend'] = self._parse_number(data['ldiv'])
            stock_data['yield'] = self._parse_number(data['dy'])
            stock_data['earnings_per_share'] = self._parse_number(data['eps'])
            stock_data['shares'] = data['shares']
            return stock_data
        except Exception as e:
            pass

    def _get_financial_table(self, report_type, term):
        assert term in ('interim', 'annual')
        assert report_type in ('inc', 'bal', 'cas')

        if not self._financial:
            self._financial = self._get_from_google()

        div_id = report_type + term + 'div'
        return self._financial('div#{} table#fs-table'.format(div_id))

    def _statement(self, statement_type, term):
        table = self._get_financial_table(statement_type, term)
        statement_line = []
        for row in table.items('tr'):
            data = [self._parse_number(i.text()) for i in row.items('th, td')]
            if not statement_line:
                data = [self._parse_date(e) for e in data]
            statement_line.append(data)
        return statement_line

    def income_statement(self, term='annual'):
        return self._statement('inc', term)

    def balance_sheet(self, term='annual'):
        return self._statement('bal', term)

    def cash_flow(self, term='annual'):
        return self._statement('cas', term)

    def stock_data(self):
        return self._get_stock_data()
