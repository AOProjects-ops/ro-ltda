"""
Configuración de la aplicación — RO LTDA (sitio v2).
Las credenciales sensibles siempre se leen de variables de entorno.
"""
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "cambia-esta-clave-en-produccion")
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(basedir, 'ro.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Datos de la empresa ---
    COMPANY_NAME = "RO"
    COMPANY_LEGAL_NAME = "RO LTDA"
    COMPANY_TAGLINE = "Conectamos talento, tecnología y estrategia. Impulsamos resultados"
    COMPANY_EMAIL = os.environ.get("COMPANY_EMAIL", "contacto@roltda.com")
    COMPANY_PHONE = os.environ.get("COMPANY_PHONE", "+57 300 000 0000")
    COMPANY_WHATSAPP = os.environ.get("COMPANY_WHATSAPP", "573000000000")
    COMPANY_ADDRESS = os.environ.get("COMPANY_ADDRESS", "La Guajira, Colombia")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
