import csv
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, InputRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField


def validate_input(form, field):
    if field.data.isnumeric():
        raise ValidationError('Please enter only letters and numbers')


def validate_input_is_numeric(form, field):
    if type(field) != int and type(field) != float:
        raise ValidationError('Please enter numbers only')


def validate_stock(form, field):
    ticker_list = []
    with open('data/tickers.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            ticker_list.append(i[1])
    if field not in ticker_list:
        raise ValidationError(f'Stock symbol {field} was not found')


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[DataRequired(), Regexp(r'^[a-z]', message='Only a to z allowed')])
    purchase_price = IntegerField('Price at Purchase',
                                  validators=[DataRequired(), Length(min=0)])
    num_of_shares = IntegerField('Number of Shares',
                                 validators=[DataRequired(), Length(min=0)])
    submit = SubmitField('Add Stock')


class LoginForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email(), validate_input])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationsForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email(), validate_input])
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm password*',
                                     validators=[DataRequired(), Length(min=5, max=20),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
