from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.stock import Stock
from models.user import User
from forms.forms import RegistrationsForm, AddStockForm, LoginForm

stocks_blueprint = Blueprint('stocks', __name__)


@stocks_blueprint.route('/table', methods=['GET', 'POST'])
def table():
    stocks = Stock.get_all_stocks()
    total = Stock.get_total()
    form = AddStockForm()
    return render_template('stocks/table.html', stocks=stocks, Stock=Stock, total=total, form=form)


@stocks_blueprint.route('/add_stock', methods=['POST'])
def add_stock():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        num_of_shares = request.form['num_of_shares']
        purchase_price = request.form['purchase_price']
        Stock(stock_symbol, num_of_shares, purchase_price).save_to_mongo()
        return redirect(url_for('stocks.table'))


@stocks_blueprint.route('/remove_stock', methods=['POST'])
def remove_stock():
    if request.method == 'POST':
        stock_id = request.form['stock_id']
        Stock.remove_from_mongo(stock_id)
        return redirect(url_for('stocks.table'))


@stocks_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationsForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        User(email, password).save_to_mongo()
        flash('Account created, you can log in now', 'success')
        return redirect(url_for('stocks.login'))
    else:
        return render_template('stocks/register.html', form=form)


@stocks_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'a' and form.password.data == 'a':
            flash('Login Success', 'success')
            return redirect(url_for('stocks.index'))
        # else:
        #     flash('Wrong')
    return render_template('stocks/login.html', form=form)


@stocks_blueprint.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('stocks/about.html')
