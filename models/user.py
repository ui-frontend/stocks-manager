import uuid
from common.database import StockDatabase


class User:
    def __init__(self, username, password, email, _id):
        self.username = username
        self.password = password
        self.email = email
        self._id = _id or uuid.uuid4().hex

    def save_to_mongo(self):
        StockDatabase.insert(self.collection, self.get_stock_data())
