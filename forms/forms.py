from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, InputRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField


def validate_input(form, field):
    if field.data.isnumeric():
        raise ValidationError('Please enter only letters and numbers')


def validate_input_is_numeric(form, field):
    if type(field) != int and type(field) != float:
        raise ValidationError('Please enter numbers only')


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[DataRequired(), Regexp(r'^[a-z]', message='Only a to z allowed')])
    purchase_price = IntegerField('Price at Purchase',
                                  validators=[DataRequired(), Length(min=0)])
    num_of_shares = IntegerField('Number of Shares',
                                 validators=[DataRequired(), Length(min=0)])
    submit = SubmitField('Add Stock')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), validate_input])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


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
