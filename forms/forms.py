from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol', validators=[DataRequired()])
    price_at_purchase = IntegerField('Price at Purchase', validators=[DataRequired(), Length(min=0)])
    shares = IntegerField('Number of Shares', validators=[DataRequired(), Length(min=0)])


class RegistrationsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), Length(min=5, max=20), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

