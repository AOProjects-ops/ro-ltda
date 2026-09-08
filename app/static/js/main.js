// RO — interacciones básicas del sitio
document.addEventListener("DOMContentLoaded", function () {
  // Mostrar el modal de bienvenida solo una vez por sesión de navegación:
  // la primera vez que se entra al sitio, o al recargar (F5). Si el usuario
  // navega entre páginas dentro de la misma pestaña, no se repite.
  const welcomeModalEl = document.getElementById("welcomeModal");
  if (welcomeModalEl) {
    const yaSeMostro = sessionStorage.getItem("ro_welcome_modal_shown");
    if (!yaSeMostro) {
      const welcomeModal = new bootstrap.Modal(welcomeModalEl);
      setTimeout(() => welcomeModal.show(), 600);
      sessionStorage.setItem("ro_welcome_modal_shown", "1");
    }
  }

  const links = document.querySelectorAll(".navbar-ro .nav-link");
  links.forEach((link) => {
    if (link.getAttribute("href") === window.location.pathname) {
      link.classList.add("active");
    }
  });

  const navbarCollapse = document.getElementById("navbarRO");
  document.querySelectorAll(".navbar-ro .nav-link, .navbar-ro .dropdown-item").forEach((link) => {
    link.addEventListener("click", () => {
      if (navbarCollapse.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
      }
    });
  });

  // --- Galería de fotos del equipo: rotación aleatoria cada 15s -----------
  // Elige 4 fotos distintas de window.RO_GALLERY_IMAGES para los 4 recuadros
  // (#gallery-slot-0..3) y las va reemplazando con un fundido suave.
  const gallerySlots = [0, 1, 2, 3]
    .map((i) => document.getElementById("gallery-slot-" + i))
    .filter(Boolean);

  if (gallerySlots.length && Array.isArray(window.RO_GALLERY_IMAGES) && window.RO_GALLERY_IMAGES.length) {
    const allImages = window.RO_GALLERY_IMAGES;
    const baseUrl = window.RO_GALLERY_BASE_URL || "";

    // Devuelve N nombres de archivo distintos, tomados al azar del catálogo.
    function pickRandomDistinct(pool, n) {
      const copy = pool.slice();
      const picked = [];
      const count = Math.min(n, copy.length);
      for (let i = 0; i < count; i++) {
        const idx = Math.floor(Math.random() * copy.length);
        picked.push(copy.splice(idx, 1)[0]);
      }
      return picked;
    }

    function swapGallery() {
      const nextImages = pickRandomDistinct(allImages, gallerySlots.length);
      gallerySlots.forEach((imgEl, i) => {
        if (!nextImages[i]) return;
        imgEl.classList.add("fading");
        setTimeout(() => {
          imgEl.src = baseUrl + nextImages[i];
          imgEl.classList.remove("fading");
        }, 350);
      });
    }

    setInterval(swapGallery, 15000);
  }

  // --- Lightbox: ampliar cualquier foto marcada como "lightbox-trigger" ---
  const lightboxModalEl = document.getElementById("lightboxModal");
  if (lightboxModalEl) {
    const lightboxModal = new bootstrap.Modal(lightboxModalEl);
    const lightboxImage = document.getElementById("lightboxImage");

    document.addEventListener("click", function (e) {
      const trigger = e.target.closest(".lightbox-trigger");
      if (!trigger) return;
      const nestedImg = trigger.querySelector("img");
      const fullSrc = (nestedImg && nestedImg.src) || trigger.dataset.fullSrc;
      if (!fullSrc) return;
      lightboxImage.src = fullSrc;
      lightboxModal.show();
    });
  }
});
