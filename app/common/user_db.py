from app import db


class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    stock_info = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.email}"
