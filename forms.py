"""
Formularios con Flask-WTF: token CSRF automático + validación de
cada campo en el servidor (WTForms), nunca solo en el navegador.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp, Optional

from app.content import ALL_SERVICES


class ContactForm(FlaskForm):
    name = StringField(
        "Nombre completo",
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=2, max=120)],
    )
    email = StringField(
        "Correo electrónico",
        validators=[DataRequired(message="El correo es obligatorio."), Email(message="Correo inválido."), Length(max=120)],
    )
    phone = StringField(
        "Teléfono (opcional)",
        validators=[Optional(), Regexp(r"^[0-9+\-\s()]{7,20}$", message="Teléfono inválido.")],
    )
    company = StringField(
        "Empresa (opcional)",
        validators=[Optional(), Length(max=150)],
    )
    service_interest = SelectField(
        "Servicio de interés",
        choices=[("Información general", "Información general")] + [(s, s) for s in ALL_SERVICES],
        validators=[DataRequired()],
    )
    message = TextAreaField(
        "Cuéntanos tu necesidad",
        validators=[DataRequired(message="Escribe tu mensaje."), Length(min=10, max=2000)],
    )
