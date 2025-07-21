from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PresupuestoForm(FlaskForm):
    nombre = StringField('Nombre del presupuesto', validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=100)
    ])
    año = IntegerField('Año', validators=[
        validators.DataRequired(),
        validators.NumberRange(min=2020, max=2100)
    ])