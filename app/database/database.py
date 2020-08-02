from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"


class StockDb(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    full_name = db.Column(db.String(120))
    stock_symbol = db.Column(db.String(120))
    shares = db.Column(db.Float(120))
    purchase_price = db.Column(db.Float(120))
    net_buy_price = db.Column(db.Float(120))
    logo = db.Column(db.String(120))

    # def __repr__(self):
    #     return f'Stock symbol: {self.stock_symbol}, Shares: {self.shares}, Purchase price: {self.purchase_price}'
