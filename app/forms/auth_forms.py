from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired("El email es obligatorio"),
        Email("Ingrese un email válido")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired("La contraseña es obligatoria"),
        Length(min=6, message="Mínimo 6 caracteres")
    ])
    remember = BooleanField('Recordar sesión')