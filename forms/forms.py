from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, InputRequired
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[DataRequired(), Regexp(r'^[a-z]', message='Only a to z allowed')])
    purchase_price = IntegerField('Price at Purchase', validators=[DataRequired(), Length(min=0)])
    num_of_shares = IntegerField('Number of Shares', validators=[DataRequired(), Length(min=0)])
    submit = SubmitField('Add Stock')


class RegistrationsForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), Length(min=5, max=20),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
