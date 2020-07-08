from typing import Dict
import pymongo


class StockDatabase:
    URI = f'mongodb://127.0.0.1:27017/stocks'
    DATAB = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        StockDatabase.DATAB[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return StockDatabase.DATAB[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return StockDatabase.DATAB[collection].find_one(query)

    @staticmethod
    def remove(collection: str, query: Dict):
        return StockDatabase.DATAB[collection].remove(query)


class AlertDatabase:
    URI = f'mongodb://127.0.0.1:27017/alerts'
    DATAB = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        AlertDatabase.DATAB[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return AlertDatabase.DATAB[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return AlertDatabase.DATAB[collection].find_one(query)

    @staticmethod
    def remove(collection: str, query: Dict):
        return StockDatabase.DATAB[collection].remove(query)

