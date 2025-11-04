from wtforms import Form
from flask_wtf import FlaskForm 
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, NumberRange, Email
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula',
    [validators.DataRequired(message="La matricula es obligatoria")])
    nombre = StringField('Nombre',
    [validators.DataRequired(message="El nombre es obligatorio")])
    apellido = StringField('Apellido',
    [validators.DataRequired(message="El apellido es obligatorio")])
    email = EmailField('Email',
    [validators.Email(message="El email no es valido")
    ])

class FiguraForm(Form):
    figura = RadioField('Figura', choices=[
        ('triangulo', 'Triángulo'),
        ('rectangulo', 'Rectángulo'),
        ('circulo', 'Círculo'),
        ('pentagono', 'Pentágono')
    ], validators=[validators.DataRequired(message="Selecciona una figura")])
    valor1 = FloatField('Valor 1',
    [validators.DataRequired(message="El valor 1 es obligatorio")])
    valor2 = FloatField('Valor 2',
    [validators.DataRequired(message="El valor 2 es obligatorio")])