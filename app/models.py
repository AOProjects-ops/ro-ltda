"""
Modelos de datos. SQLAlchemy (ORM) parametriza automáticamente las
consultas, evitando inyección SQL.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ContactMessage(db.Model):
    """Mensaje enviado desde el formulario de contacto público."""

    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    company = db.Column(db.String(150), nullable=True)
    service_interest = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<ContactMessage {self.id} - {self.email}>"
