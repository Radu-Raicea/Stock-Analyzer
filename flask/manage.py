
from project import create_app, logger
from flask_script import Manager
import coverage
import unittest

logger.info('Server has started.')

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'tests/*',
        'project/website/*',
        'project/__init__.py'
    ]
)
COV.start()

app = create_app()
manager = Manager(app)


@manager.command
def cov():
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    else:
        return 1


@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@manager.command
def test_one(test_file):
    tests = unittest.TestLoader().discover('tests', pattern=test_file + '.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@manager.command
def finance(market, ticker):

    from project.services.google_finance import GoogleFinance

    google_finance = GoogleFinance(market, ticker)
    report = google_finance.balance_sheet()
    for x in report:
        print(x, flush=True)

if __name__ == '__main__':
    manager.run()
