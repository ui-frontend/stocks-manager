import csv
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, InputRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from app.database.database import User


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[DataRequired(), Regexp(r'^[a-z]', message='Only a to z allowed')])
    purchase_price = IntegerField('Price at Purchase',
                                  validators=[DataRequired(), Length(min=0)])
    num_of_shares = IntegerField('Number of Shares',
                                 validators=[DataRequired(), Length(min=0)])
    submit = SubmitField('Add Stock')


class LoginForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationsForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm password*',
                                     validators=[DataRequired(), Length(min=5, max=20),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

    # def validate_email(self, email):
    #     user = UserDb.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('Email already in use')
