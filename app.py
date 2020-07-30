from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from views.stocks import stocks_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '6c9a0af7a220762b3ec7d435b3ff14a4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"{self.email}"

class Temp:
    def __init__(self):
        pass



app.register_blueprint(stocks_blueprint, url_prefix='/stocks')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
