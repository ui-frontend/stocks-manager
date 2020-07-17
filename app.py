from flask import Flask, url_for
from views.stocks import stocks_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = '6c9a0af7a220762b3ec7d435b3ff14a4'

app.register_blueprint(stocks_blueprint, url_prefix='/stocks')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
