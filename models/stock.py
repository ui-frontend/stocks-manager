import csv
import uuid
import yfinance as yf
from wallstreet import Stock as WS
from pprint import pprint
from typing import Dict, List
from common.database import StockDatabase


class Stock:
    collection = 'stocks'

    def __init__(self, stock_symbol: str, number_of_shares: float, purchase_price: float, _id: str = None):
        self._id = _id or uuid.uuid4().hex
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
        self.tickers = list(self._load_all_tickers())
        self.logos = list(self._load_all_logos())
        self.stock_data = self._add_stock(stock_symbol)

    def save_to_mongo(self):
        StockDatabase.insert(self.collection, self.get_stock_data())

    def remove_from_mongo(id):
        StockDatabase.remove('stocks', id)

    def get_logo_url(self, stock_symbol):
        for logo in self.logos:
            if logo['company'] == stock_symbol:
                return logo['logo']
        return 'https://cdn2.iconfinder.com/data/icons/growth-bar-vol-3/512/41-512.png'

    def _add_stock(self, stock_symbol) -> Dict:
        stock_symbol = stock_symbol.upper()
        for ticker in self.tickers:

            if ticker['symbol'] == stock_symbol:
                full_name = ticker['company']

                return dict(
                    _id=self._id,
                    full_name=full_name,
                    stock_symbol=stock_symbol,
                    shares=float(self.number_of_shares),
                    purchase_price=float(self.purchase_price),
                    net_buy_price=round(float(self.number_of_shares) * float(self.purchase_price), 2),
                    logo=self.get_logo_url(stock_symbol)
                )

    def get_stock_data(self) -> Dict:
        """{'_id': 'c7d3a63e899f46f98ed7b6913396a708', 'full_name': 'NVIDIA Corporation',
        'stock_symbol': 'NVDA', 'shares': 12.0, 'purchase_price': 351.0, 'net_buy_price': 4212.0}"""
        return self.stock_data

    @staticmethod
    def _load_all_tickers():
        with open('data/tickers.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                yield dict(company=i[0], symbol=i[1])

    @staticmethod
    def _load_all_logos():
        with open('data/logo.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                yield dict(company=i[0], logo=i[1])

    @staticmethod
    def get_current_stock_price_by_symbol(stock_symbol) -> float:
        upper_stock_symbol = stock_symbol.upper()
        return WS(upper_stock_symbol).price

    @classmethod
    def get_yield_of_single_stock(cls, stock) -> List:
        stock_data = stock.get_stock_data()

        num_of_shares = stock_data['shares']
        stock_symbol = stock_data['stock_symbol']
        purchase_price = stock_data['purchase_price']
        current_price = cls.get_current_stock_price_by_symbol(stock_symbol)

        profit_in_usd = (current_price - purchase_price) * num_of_shares
        profit_prec = (current_price - purchase_price) / purchase_price * 100
        total_value = num_of_shares * current_price

        return dict(symbol=stock_symbol,
                    profit_in_usd=round(profit_in_usd, 2),
                    profit_prec=round(profit_prec, 2),
                    total_value=round(total_value, 2))

    @classmethod
    def get_all_stocks(cls) -> List:
        """return a list of class objects"""
        db_stocks = StockDatabase.find('stocks', {})
        return [cls(stock['stock_symbol'], stock['shares'], stock['purchase_price'], stock['_id']) for stock in
                db_stocks]

    @classmethod
    def get_total(cls):

        quantity = 0
        value = 0
        profit_loss = 0

        stocks = Stock.get_all_stocks()
        for stock in stocks:
            stock_data = stock.get_stock_data()
            stock_yeild = stock.get_yield_of_single_stock(stock)

            quantity += stock_data['shares']
            value += stock_yeild['total_value']
            profit_loss += stock_yeild['profit_in_usd']

        return dict(quantity=round(quantity, 2), value=round(value, 2), profit_loss=round(profit_loss, 2))
