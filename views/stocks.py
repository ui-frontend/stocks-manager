from flask import Blueprint, render_template, request, redirect, url_for
from models.stock import Stock
from forms.forms import RegistrationsForm, AddStockForm

stocks_blueprint = Blueprint('stocks', __name__)


@stocks_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    stocks = Stock.get_all_stocks()
    total = Stock.get_total()
    form = AddStockForm()
    return render_template('stocks/index.html', stocks=stocks, Stock=Stock, total=total, form=form)


# @stocks_blueprint.route('/add_stock', methods=['POST'])
# def add_stock():
#     if request.method == 'POST':
#         stock_symbol = request.form['stock_symbol']
#         num_of_shares = request.form['num_of_shares']
#         purchase_price = request.form['purchase_price']
#         Stock(stock_symbol, num_of_shares, purchase_price).save_to_mongo()
#         return redirect(url_for('stocks.index'))


#using WTForms
@stocks_blueprint.route('/add_stock', methods=['POST'])
def add_stock():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        num_of_shares = request.form['num_of_shares']
        purchase_price = request.form['purchase_price']
        Stock(stock_symbol, num_of_shares, purchase_price).save_to_mongo()
        return redirect(url_for('stocks.index'))



@stocks_blueprint.route('/register', methods=['POST'])
def register():
    form = RegistrationsForm()
    return render_template('stocks/register.html', form=form)


@stocks_blueprint.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    return render_template('stocks/login.html', form=form)
