"""
Application factory — RO LTDA, sitio web v2.
"""
import os
from datetime import datetime
from flask import Flask
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.config import config_by_name
from app.models import db

csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])


def create_app(config_name=None):
    config_name = config_name or os.environ.get("FLASK_ENV", "default")

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        return response

    from app.views.main import main_bp
    app.register_blueprint(main_bp)

    from app.content import SERVICE_CATEGORIES

    @app.context_processor
    def inject_company_info():
        return {
            "company_name": app.config["COMPANY_NAME"],
            "company_legal_name": app.config["COMPANY_LEGAL_NAME"],
            "company_tagline": app.config["COMPANY_TAGLINE"],
            "company_email": app.config["COMPANY_EMAIL"],
            "company_phone": app.config["COMPANY_PHONE"],
            "company_whatsapp": app.config["COMPANY_WHATSAPP"],
            "company_address": app.config["COMPANY_ADDRESS"],
            "current_year": datetime.utcnow().year,
            "service_categories": SERVICE_CATEGORIES,
        }

    with app.app_context():
        db.create_all()

    return app
