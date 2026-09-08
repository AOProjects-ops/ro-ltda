"""
Rutas del sitio corporativo de RO LTDA (v2).
"""
import random

from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request

from app.forms import ContactForm
from app.models import db, ContactMessage
from app.content import (
    MISSION, VISION, ABOUT_INTRO, HISTORY, OBJECTIVES, VALUES,
    SUCCESS_FACTORS, CLIENTS, SERVICE_CATEGORIES, STATS,
    GALLERY_IMAGES, HERO_IMAGE,
)
from app import limiter

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    shuffled_gallery = GALLERY_IMAGES.copy()
    random.shuffle(shuffled_gallery)
    return render_template(
        "index.html",
        mission=MISSION,
        vision=VISION,
        about_intro=ABOUT_INTRO,
        values=VALUES,
        stats=STATS,
        clients=CLIENTS,
        service_categories=SERVICE_CATEGORIES,
        gallery_images=shuffled_gallery,
        hero_image=HERO_IMAGE,
        form=ContactForm(),
    )


@main_bp.route("/nosotros")
def about():
    return render_template(
        "about.html",
        mission=MISSION,
        vision=VISION,
        about_intro=ABOUT_INTRO,
        history=HISTORY,
        objectives=OBJECTIVES,
        values=VALUES,
        success_factors=SUCCESS_FACTORS,
        clients=CLIENTS,
    )


@main_bp.route("/servicios")
def services():
    return render_template("services.html", service_categories=SERVICE_CATEGORIES)


@main_bp.route("/galeria")
def gallery():
    # La foto de equipo del hero aparece primero, seguida del resto en orden aleatorio.
    rest = GALLERY_IMAGES.copy()
    random.shuffle(rest)
    return render_template(
        "gallery.html",
        gallery_images=rest,
        hero_image=HERO_IMAGE,
    )


@main_bp.route("/contacto", methods=["GET", "POST"])
@limiter.limit("5 per minute")  # anti-spam: máx 5 envíos por minuto por IP
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        nuevo_mensaje = ContactMessage(
            name=form.name.data.strip(),
            email=form.email.data.strip(),
            phone=(form.phone.data or "").strip(),
            company=(form.company.data or "").strip(),
            service_interest=form.service_interest.data,
            message=form.message.data.strip(),
        )
        db.session.add(nuevo_mensaje)
        db.session.commit()

        current_app.logger.info("Nuevo mensaje de contacto de %s", nuevo_mensaje.email)
        flash("¡Gracias por escribirnos! Un asesor de RO te contactará muy pronto.", "success")

        # Si el formulario se envió desde otra página (ej. el mini-formulario
        # del inicio), regresamos ahí en vez de siempre ir a /contacto.
        next_path = request.form.get("next", "")
        if next_path.startswith("/") and not next_path.startswith("//"):
            return redirect(next_path)
        return redirect(url_for("main.contact"))

    return render_template("contact.html", form=form)


@main_bp.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404
