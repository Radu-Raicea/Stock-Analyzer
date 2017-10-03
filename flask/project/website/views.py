
from flask import render_template, Blueprint, request, redirect
from project.services.stocks import add_stock, get_stocks_from_google, remove_stock, get_stocks_from_db
import json

website_blueprint = Blueprint('website_blueprint', __name__)


@website_blueprint.route('/')
def index():
    stocks = get_stocks_from_db()
    if stocks:
        return render_template('index.html', stocks=stocks)
    else:
        return render_template('index.html', stocks=[])


@website_blueprint.route('/stocks')
def stocks():
    stocks = get_stocks_from_google()
    return json.dumps(stocks, default=lambda number: float(number))


@website_blueprint.route('/add/<string:market>/<string:ticker>', methods=['POST'])
def add(market, ticker):
    add_stock(market, ticker)
    return redirect('/')


@website_blueprint.route('/remove/<string:market>/<string:ticker>', methods=['POST'])
def remove(market, ticker):
    remove_stock(market, ticker)
    return redirect('/')
