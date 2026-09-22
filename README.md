# Sitio web corporativo v2 — RO LTDA

Segunda versión del sitio, **desarrollada desde cero** con una estructura de
información y un diseño distintos a la primera entrega: inspirada en la
organización de **humancapital-hc.com** (hero con propuesta de valor + "píldoras"
de proceso, portafolio de soluciones por categoría, franja de indicadores,
franja de clientes y CTA de contacto), pero con la identidad visual y el
contenido real de **RO LTDA**.

A diferencia de la primera versión, el contenido (misión, visión, valores,
historia, objetivos, factores de éxito y los 21 servicios) ya no es de
ejemplo: fue extraído directamente de `SERVICIOS_PORTAFOLIO_RO.docx` y
`PORTAFOLIO_RO.pptx`.

## 📁 Estructura del proyecto

```
ro_web_v2/
├── app/
│   ├── __init__.py        # Application factory (extensiones, headers de seguridad, blueprints)
│   ├── config.py           # Configuración por entorno (dev/producción)
│   ├── content.py          # Contenido institucional real de RO (misión, valores, 21 servicios, etc.)
│   ├── models.py           # Modelo SQLAlchemy del formulario de contacto
│   ├── forms.py             # Formulario WTForms (validación + CSRF)
│   ├── views/
│   │   └── main.py         # Rutas: inicio, nosotros, servicios, contacto
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html      # Hero, estadísticas, misión/visión, valores, portafolio, clientes, CTA
│   │   ├── about.html      # Historia, objetivos, valores, factores de éxito, clientes
│   │   ├── services.html   # Acordeón con los 21 servicios agrupados en 5 categorías
│   │   ├── contact.html
│   │   ├── 404.html
│   │   └── includes/
│   │       ├── navbar.html # Con dropdown de categorías de servicios
│   │       └── footer.html # Con botón flotante de WhatsApp
│   └── static/
│       ├── css/style.css   # Diseño "consultora" (hero oscuro) con la paleta del logo de RO
│       ├── js/main.js
│       └── img/            # logo.png y ro-hero.png
├── requirements.txt
├── run.py
├── .env.example
└── .gitignore
```

## ⚙️ Instalación y ejecución en local

```bash
cd ro_web_v2
python3 -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # y define tu propio SECRET_KEY
python run.py
```

El sitio queda disponible en **http://localhost:5000**. La base SQLite
(`ro.db`) se crea automáticamente y ahí quedan los mensajes del formulario
de contacto.

## 🚀 Despliegue en producción

```bash
gunicorn -w 4 -b 0.0.0.0:8000 "run:app"
```

Define `FLASK_ENV=production`, sirve detrás de HTTPS, y cambia
`DATABASE_URL` a Postgres/MySQL si esperas tráfico alto.

## 🔐 Seguridad implementada

| Riesgo | Mitigación |
|---|---|
| CSRF | `Flask-WTF` — token oculto en el formulario de contacto |
| Inyección SQL | SQLAlchemy (ORM), sin SQL manual |
| XSS | Auto-escape de Jinja2 |
| Validación de entrada | `WTForms` valida en el servidor |
| Spam / fuerza bruta | `Flask-Limiter`: 5 envíos/min por IP |
| Cabeceras HTTP | `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy` |
| Cookies de sesión | `HttpOnly`, `SameSite=Lax`, `Secure` en producción |
| Secretos | Solo por variables de entorno |

## 🆕 Última actualización — marco de la foto con los colores del logo real

El marco decorativo detrás de la foto principal usaba colores genéricos
(morado incluido). Extraje los colores dominantes **directamente del
archivo del logo** (`logo.png`) muestreando sus píxeles, y ahora el marco
usa exactamente esos tonos: el magenta de la franja del cubo (`#E80080` →
`#A00058`) arriba, y el ámbar/naranja de las caras del cubo (`#F8C020` →
`#F07818`) abajo. Ya no aparece el morado que no está en tu logo.

## 🆕 Actualización anterior — integración del archivo de referencia que enviaste

Revisé el proyecto Flask independiente que subiste (`RO_WEB_Cerrejon.zip`).
Es una réplica fiel de la plantilla, pero con dos problemas para usarlo tal
cual como página real: usa tamaños de fuente pensados para verse igual solo
en una captura de pantalla pequeña (párrafos de 8-10px, ilegibles en un
navegador normal), y todavía tenía los datos de ejemplo de la plantilla
(teléfono, correo, valores genéricos) en vez de los tuyos.

En vez de reemplazar tu sitio por ese archivo, **integré lo que sí aporta
valor** a tu proyecto ya funcional (una sola aplicación, con tus rutas
reales, tu formulario con backend, la Galería, el lightbox, etc.):

- **Paleta de colores exacta** de tu archivo: navy `#07142E`, magenta
  `#C9006F`, naranja `#FF9700`, morado `#6B2FD8` — reemplazan los tonos
  anteriores en todo el sitio (botones, navbar, franja de servicios, marco
  del hero, degradados).
- **Íconos de "Nuestros valores"** con color individual por tarjeta (rosa,
  naranja, morado, dorado) en vez de un solo degradado repetido — igual que
  tu archivo.
- **Panel de "Información de contacto"**: los íconos ahora van dentro de una
  burbuja circular color navy, igual que en tu archivo.
- Mantuve tu logo y foto de equipo ya procesados (son el mismo contenido que
  traía tu archivo, solo que con mejor calidad), tus 21 servicios reales,
  tus 7 valores reales, y toda la funcionalidad ya construida (formulario
  con validación y CSRF, galería con 13 fotos y rotación aleatoria, lightbox
  para ampliar/descargar cualquier foto, página Galería completa).

## 🆕 Actualización anterior — hero más compacto (igual densidad que la referencia)

El hero se veía mucho más alto y disperso que la plantilla de referencia
porque el contenido real (párrafo y textos de los botones) es más largo que
el texto de ejemplo de la plantilla, y la tipografía/espaciados estaban
pensados para textos cortos. Se ajustó para lograr la misma **densidad
visual**, sin acortar tu contenido real:

- Título (H1) y párrafo con tamaño de fuente más pequeño.
- Botones más compactos y en la misma línea (antes se apilaban uno debajo
  del otro porque no cabían con el tamaño anterior).
- Menos espacio en blanco vertical entre bloques.
- La columna de la foto se ajusta a la nueva altura, más corta.

## 🆕 Actualización anterior — forma exacta del marco decorativo (SVG)

A partir de la imagen que enviaste con la forma recortada, medí sus
coordenadas píxel por píxel y reconstruí el marco como un **SVG con la
silueta exacta** (dos bandas en zigzag tipo "rayo", con el mismo quiebre y
los mismos colores degradados: morado→magenta arriba, ámbar→ámbar oscuro
abajo), en lugar de las formas aproximadas de antes.

Sigue anclado con tamaño **fijo en píxeles** a la esquina de la foto (no
depende del alto del texto), así que se mantiene igual de nítido en
cualquier ancho de pantalla — lo probé en 1280px, 1440px, 1920px y 2400px.

## 🆕 Actualización anterior — corrección del marco del hero

El marco diagonal detrás de la foto se rompía en pantallas anchas o cuando
el párrafo de texto era largo: se estiraba y terminaba cruzando por encima
de toda la foto en vez de quedar como un detalle discreto en la esquina.

**Causa:** el marco usaba una altura en porcentaje (`130%`) del alto de la
fila del hero, y esa fila crece según el texto. Con `skewX()` aplicado a un
elemento muy alto, el desplazamiento horizontal se disparaba y el marco
terminaba enorme y desalineado.

**Solución:** el marco ahora son dos formas de **tamaño fijo en píxeles**
(recortadas con `clip-path`, no con `skew`), ancladas a la esquina superior
izquierda de la foto — igual que en la plantilla. Ya no dependen del alto
del texto, así que se ven igual de bien sin importar cuánto texto tenga el
párrafo o qué tan ancha sea la pantalla. Se probó en 1280px, 1440px, 1920px
y 2400px de ancho.

## 🆕 Actualización anterior — reconstrucción estructural del inicio

Se reconstruyó la portada (`index.html`) línea por línea para seguir
**exactamente** la estructura de la plantilla de referencia (misma
composición, mismo orden de secciones, mismo formato de tarjetas),
manteniendo la paleta de colores de RO:

- **Hero "a sangre"**: la foto de equipo ahora ocupa toda la altura del hero
  y llega hasta el borde derecho de la pantalla (ya no tiene bordes
  redondeados ni sombra). El texto queda a la izquierda dentro de un ancho
  fijo, con una cinta diagonal con los colores de marca detrás de la costura
  entre texto y foto, una insignia flotante sobre la foto ("Talento humano
  con propósito"), y puntos indicadores decorativos bajo los botones. Se
  quitaron los 3 recuadros de "Diagnóstico / Solución a la medida /
  Confidencialidad" que no estaban en la plantilla.
- **Franja "Nuestros servicios"** oscura, inmediatamente después del hero
  (se quitó la franja de estadísticas numéricas que estaba ahí antes).
  Las tarjetas ahora tienen un ícono circular de color (rotando entre
  magenta/ámbar/morado/dorado) y un borde inferior del mismo color, igual
  que la plantilla.
- **Fila "Valores + Formulario de contacto + Información de contacto"**
  nueva, con 3 columnas: 4 valores destacados en mini-tarjetas (con enlace a
  ver los 7 completos en Nosotros), un formulario compacto embebido que
  envía a la misma ruta `/contacto` y te devuelve al inicio después de
  enviarlo, y un panel naranja con teléfono, correo, dirección y horario.
- **Footer de una sola línea**: logo + copyright a la izquierda, íconos de
  redes sociales al centro, enlaces legales a la derecha — igual que la
  plantilla (antes tenía 3 columnas con enlaces de navegación).
- La sección de **Galería** (4 fotos aleatorias) se mantiene en el inicio,
  ya que fue un pedido explícito tuyo en un paso anterior y la plantilla no
  la contradice, solo no la incluye.

## 🆕 Actualización anterior

- **Navbar oscuro de nuevo** (en vez del blanco de la actualización anterior) —
  se creó una segunda versión del logo con el texto en blanco
  (`app/static/img/logo-dark-bg.png`) para que se lea bien sobre fondo oscuro;
  el logo original con texto negro (`logo.png`) se sigue usando para el
  favicon y las vistas previas al compartir el sitio.
- **Botón de WhatsApp en el navbar** ("Escríbenos por WhatsApp"), estilo pill,
  visible en todas las páginas.
- **Página "Galería" nueva** (`/galeria`, enlazada en el menú) — muestra la
  foto de equipo completo más las 12 fotos individuales en una cuadrícula.
- **Lightbox en todas las fotos**: la foto del hero, los 4 recuadros de la
  Galería en el home, y cada foto de la página `/galeria` se pueden ampliar
  con un clic (ventana modal) y descargar con el botón "Descargar foto". El
  mecanismo es genérico (clase `.lightbox-trigger` en `main.js`) — cualquier
  foto nueva que agregues con esa clase queda ampliable/descargable
  automáticamente.
- **Hero rediseñado** como página de aterrizaje premium: fondo claro con
  textura de puntos, franja diagonal con los colores de marca detrás de la
  foto de equipo (ahora más grande), insignia flotante "Más de 20 años de
  trayectoria", y la sección de Portafolio con banda oscura para dar más
  contraste y jerarquía visual.

## 🆕 Actualización anterior

- **Logo oficial actualizado** — se reemplazó el logo anterior por el archivo
  oficial que enviaste (cubo + "RO LTDA" en negro, fondo transparente). Como
  el texto es negro, el **navbar cambió a fondo blanco** (antes oscuro) para
  que se lea correctamente; en el footer (que sigue oscuro) el logo va dentro
  de una placa blanca.
- **Sección "Galería RO"** nueva en la portada: 4 recuadros que muestran fotos
  reales del equipo, elegidas al azar entre 12 fotos y con el orden inicial
  también aleatorio en cada carga de página. Rotan automáticamente cada 15
  segundos con un fundido suave, sin repetir foto entre los 4 recuadros al
  mismo tiempo. Las fotos viven en `app/static/img/gallery/`; para agregar o
  quitar fotos, edita la lista `GALLERY_IMAGES` en `app/content.py`.
- **Foto real del equipo en el hero** — la foto de grupo (14 personas) que
  identificaste como la principal ahora es la imagen grande de la portada,
  en `app/static/img/hero/team-hero.jpg`, reemplazando el gráfico de stock.
- **Nuevos eslóganes** aplicados: el titular de la portada (H1), el título
  del modal "Cotiza con nosotros", y el tagline general de la empresa
  (meta descripción SEO y footer) — los tres editables en `app/content.py`
  y `app/config.py` (`COMPANY_TAGLINE`).

## 🆕 Actualización anterior

- **Logo real de RO** incorporado (recortado con fondo transparente a partir
  del archivo que enviaste), reemplazando el logo temporal anterior. Se usa
  en el navbar, el footer y el favicon.
- **Modal de bienvenida automático**, igual al de la página de referencia
  (humancapital-hc.com): aparece al entrar a cualquier página, con las 5
  categorías de servicio de RO como accesos rápidos y botones a "Ver
  portafolio completo" / "Ir a Contacto". Incluye un botón flotante
  ("✨ Cotiza aquí") que lo vuelve a abrir en cualquier momento, junto al
  botón de WhatsApp.
- **Bootstrap y Bootstrap Icons ahora están incluidos localmente** en
  `app/static/vendor/` en vez de cargarse desde un CDN — el sitio funciona
  igual sin depender de conexión a un servicio externo.

## 🧭 Qué cambia frente a la primera versión

- **Estructura**: navbar con dropdown de categorías de servicios (como en la
  referencia), hero oscuro con 3 "píldoras" de proceso, franja de
  estadísticas, sección de portafolio por categoría, franja de clientes
  reales (Cerrejón, Cerromatoso), acordeón de servicios en vez de tarjetas
  simples, y botón flotante de WhatsApp.
- **Contenido**: 100% tomado de tus documentos — ya no es de ejemplo.
- **Diseño**: paleta igual (ámbar/magenta/morado del logo), pero con hero y
  navbar oscuros, tarjetas con borde en vez de sombra pesada, y tipografía
  Manrope en vez de Poppins, para que se sienta como un sitio distinto.

## ✏️ Cómo personalizar más

- Todo el contenido institucional (misión, visión, valores, historia,
  objetivos, factores de éxito, clientes y los 21 servicios) está en
  `app/content.py`, en español y organizado por bloques — edítalo
  directamente ahí.
- Datos de contacto (correo, teléfono, WhatsApp, dirección): `.env` o
  `app/config.py`.
- Logo: reemplaza `app/static/img/logo.png` (navbar/footer, recortado de la
  imagen que enviaste) y `app/static/img/ro-hero.png` (imagen del hero) por
  tus archivos oficiales en PNG/SVG con fondo transparente si los tienes —
  se verá aún mejor.
- El número de WhatsApp del botón flotante se define en `COMPANY_WHATSAPP`
  (formato internacional, sin "+", ej. `573001234567`) — el valor actual es
  un placeholder, actualízalo con el número real de RO.
