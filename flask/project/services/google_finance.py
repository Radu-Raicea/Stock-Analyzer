
import re
from decimal import Decimal
from datetime import date
from pyquery import PyQuery

GOOGLE_FINANCE_REPORT_TYPES = {
    'inc': 'Income Statement',
    'bal': 'Balance Sheet',
    'cas': 'Cash Flow',
}

DATE = re.compile('.*(\d{4})-(\d{2})-(\d{2}).*')


class GoogleFinance(object):

    GOOGLE_FINANCE_URL = 'https://finance.google.com/finance?q={}%3A{}&fstype=ii'

    def __init__(self, market, ticker):
        self.market = market.upper()
        self.ticker = ticker.upper()
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
        return PyQuery(self.GOOGLE_FINANCE_URL.format(self.market, self.ticker))

    def _get_table(self, report_type, term):
        assert term in ('interim', 'annual')
        assert report_type in ('inc', 'bal', 'cas')

        if not self._financial:
            self._financial = self._get_from_google()

        div_id = report_type + term + 'div'
        return self._financial('div#{} table#fs-table'.format(div_id))

    def _statement(self, statement_type, term):
        tbl = self._get_table(statement_type, term)
        ret = []
        for row in tbl.items('tr'):
            data = [self._parse_number(i.text()) for i in row.items('th, td')]
            if not ret:
                data = [self._parse_date(e) for e in data]
            ret.append(data)
        return ret

    def income_statement(self, term='annual'):
        return self._statement('inc', term)

    def balance_sheet(self, term='annual'):
        return self._statement('bal', term)

    def cash_flow(self, term='annual'):
        return self._statement('cas', term)
