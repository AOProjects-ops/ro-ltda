"""
Contenido institucional de RO LTDA.
Extraído de SERVICIOS_PORTAFOLIO_RO.docx y PORTAFOLIO_RO.pptx.
Centralizado aquí para que sea fácil de actualizar sin tocar templates.
"""

MISSION = (
    "Somos el aliado estratégico que transforma la gestión administrativa de "
    "RR.HH. a través de servicios especializados en nómina, gestión documental "
    "y selección de personal. Brindamos confianza y excelencia operativa a "
    "nuestros clientes, permitiéndoles enfocarse en el núcleo de su negocio "
    "mientras protegemos y potenciamos su capital humano."
)

VISION = (
    "Nuestra visión es consolidar a RO LTDA como el aliado estratégico más "
    "confiable del sector para el año 2030. Buscamos transformar la gestión "
    "corporativa garantizando total seguridad legal y operativa a través de la "
    "excelencia en outsourcing de nómina y procesos administrativos de "
    "Recursos Humanos. Seremos el motor de crecimiento de nuestros clientes, "
    "optimizando su gestión documental y revolucionando la atracción de "
    "talento mediante metodologías innovadoras de selección y evaluación de "
    "personal."
)

ABOUT_INTRO = (
    "En RO LTDA, guiados por nuestros principios y comprometidos con la "
    "excelencia, somos el aliado estratégico para responder a los desafíos "
    "actuales de su organización en la gestión integral del talento humano. "
    "Con más de 20 años de trayectoria y experiencia, combinamos tecnología, "
    "conocimiento experto y un enfoque profundamente humano para transformar "
    "cómo las empresas atraen, desarrollan y fidelizan a su gente, con "
    "resultados medibles y sostenibles, alineados con sus objetivos de negocio."
)

HISTORY = (
    "RO LTDA se constituyó en el departamento de La Guajira, realizando trabajos "
    "importantes y de alta confidencialidad para Carbones del Cerrejón Limited: "
    "administración del Archivo Central y Centro de Entrenamiento Mina, "
    "administración de nómina de fundaciones, apoyo al proceso de contratación "
    "de personal, soporte a procesos de nómina y beneficios de Recursos Humanos, "
    "soporte técnico a los aplicativos de estadísticas de personal, costos "
    "laborales y compensación, administración de servicios de soporte del "
    "sistema Lidera, y trazabilidad de documentación de RR.HH. También prestó "
    "servicios de organización de archivos en los departamentos de Asuntos "
    "Públicos y en el Proyecto de Expansión P-40, así como organización "
    "documental y digitalización de información del Archivo de Personal para "
    "Cerro Matoso S.A."
)

OBJECTIVES = [
    "Garantizar el soporte adecuado para que el manejo de información sea eficaz y esté acorde con las políticas de confidencialidad.",
    "Cumplir con las normas del gobierno y generar beneficios crecientes para todos los que participan en el proceso de modernización y productividad.",
    "Garantizar que la compañía cuente oportunamente con el recurso humano idóneo para desarrollar las actividades requeridas.",
    "Implementar las normas establecidas para garantizar un servicio de óptima calidad.",
    "Ser una empresa dinámica que se anticipa a los cambios del sector productivo, avanzando a la par del progreso tecnológico.",
]

VALUES = [
    {"title": "Compromiso", "icon": "bi-hand-thumbs-up", "text": "Asumimos cada reto con responsabilidad y dedicación, cumpliendo lo que prometemos y trabajando para alcanzar resultados que generen valor."},
    {"title": "Integridad", "icon": "bi-shield-check", "text": "Actuamos con honestidad, transparencia y coherencia, guiando cada decisión por principios éticos y el respeto hacia las personas."},
    {"title": "Respeto", "icon": "bi-people", "text": "Valoramos a cada persona, reconocemos sus diferencias y promovemos relaciones basadas en la empatía, la confianza y la dignidad."},
    {"title": "Responsabilidad", "icon": "bi-award", "text": "Cumplimos con nuestros compromisos y respondemos con precisión y puntualidad a nuestros clientes."},
    {"title": "Solidaridad", "icon": "bi-heart", "text": "Promovemos la colaboración y el apoyo mutuo, contribuyendo al bienestar de las personas y construyendo juntos un entorno más humano."},
    {"title": "Servicio", "icon": "bi-headset", "text": "Brindamos un servicio cercano, oportuno y de alta calidad, enfocado en comprender las necesidades de nuestros clientes y generar soluciones que aporten valor y confianza."},
    {"title": "Confidencialidad", "icon": "bi-lock", "text": "Protegemos la información con responsabilidad, discreción y ética, garantizando la confianza y seguridad de nuestros clientes y colaboradores."},
]

SUCCESS_FACTORS = [
    {"title": "Experiencia", "icon": "bi-graph-up-arrow", "text": "El personal de RO tiene amplia experiencia en sus funciones; la mayoría cuenta entre 6 y 18 años de trayectoria, lo que garantiza seguridad y confianza a nuestros clientes."},
    {"title": "Capacitación", "icon": "bi-mortarboard", "text": "Nuestro equipo está entrenado en procedimientos, políticas y en todos los requisitos legales para el cumplimiento normal de sus funciones."},
    {"title": "Confidencialidad", "icon": "bi-lock", "text": "Manejo profesional y adecuado de información altamente confidencial durante todo el desarrollo de nuestras funciones."},
    {"title": "Competitividad y productividad", "icon": "bi-speedometer2", "text": "A través de programas de capacitación y cubrimiento entre pares, contamos con un equipo altamente productivo y competente en cada cargo."},
    {"title": "Entrenamiento continuo", "icon": "bi-arrow-repeat", "text": "Capacitación constante en servicio al cliente, trabajo en equipo y relaciones interpersonales, entre otros temas clave."},
]

CLIENTS = [
    {"name": "Carbones del Cerrejón Limited", "detail": "Administración de Archivo Central, nómina de fundaciones, soporte a procesos de RR.HH. y digitalización documental."},
    {"name": "Cerro Matoso S.A.", "detail": "Organización documental y digitalización de información del Archivo de Personal."},
]

# --- Catálogo completo de servicios, agrupado en categorías ---------------
# Cada servicio conserva el texto real del documento de portafolio de RO.

SERVICE_CATEGORIES = [
    {
        "slug": "talento-humano",
        "title": "Gestión de Talento Humano",
        "icon": "bi-people-fill",
        "summary": "Atraemos, evaluamos, formamos y desarrollamos el talento de tu organización.",
        "services": [
            {
                "title": "Outsourcing de Nómina",
                "text": "Procesamiento y liquidación de nómina, administración de novedades, cálculo de prestaciones sociales y gestión de seguridad social (EPS, AFP, ARL y cajas de compensación), con un servicio seguro, eficiente, confidencial y oportuno.",
            },
            {
                "title": "Selección y Reclutamiento de Talento",
                "text": "Reclutamiento masivo y ejecutivo para cargos operativos, administrativos, profesionales, especializados y directivos: búsqueda y atracción de candidatos, filtro de hojas de vida, entrevistas, pruebas psicotécnicas y verificación de referencias.",
            },
            {
                "title": "Assessment Center",
                "text": "Evaluamos competencias clave como liderazgo, comunicación, trabajo en equipo, toma de decisiones y pensamiento estratégico, para apoyar procesos de selección, promoción interna y planes de carrera.",
            },
            {
                "title": "Formación y Desarrollo del Talento",
                "text": "Programas de formación, capacitación, entrenamiento y coaching para fortalecer competencias técnicas y comportamentales: liderazgo, comunicación, servicio al cliente y gestión del cambio.",
            },
            {
                "title": "Medición y Gestión del Clima Organizacional",
                "text": "Evaluamos la percepción de los colaboradores para identificar fortalezas, oportunidades de mejora y factores que influyen en la satisfacción y el compromiso de los equipos.",
            },
            {
                "title": "Gestión y Desarrollo del Desempeño",
                "text": "Procesos de evaluación de desempeño que valoran objetivamente el cumplimiento de objetivos, competencias y comportamientos, con planes de desarrollo individual.",
            },
            {
                "title": "Compensación Estratégica y Estructura Salarial",
                "text": "Valoración de cargos, diseño de estructuras y escalas salariales, análisis de equidad interna y de competitividad frente al mercado.",
            },
            {
                "title": "Estudios de Seguridad y Verificación de Candidatos",
                "text": "Verificación de referencias laborales y personales, y validación de información suministrada por el candidato, bajo criterios de confidencialidad y protección de datos.",
            },
            {
                "title": "Bienestar Laboral y Acompañamiento Psicosocial",
                "text": "Programas de bienestar, eventos corporativos, actividades de integración y acompañamiento psicosocial para fortalecer ambientes de trabajo saludables y humanizados.",
            },
            {
                "title": "Comunicación Estratégica y Organizacional",
                "text": "Estrategias de comunicación interna, canales y campañas corporativas para fortalecer el sentido de pertenencia y la alineación de los equipos.",
            },
        ],
    },
    {
        "slug": "gestion-documental",
        "title": "Gestión Documental",
        "icon": "bi-folder2-open",
        "summary": "Organización, digitalización y administración eficiente de la información de tu empresa.",
        "services": [
            {
                "title": "Soluciones Integrales en Gestión Documental",
                "text": "Organización y clasificación de archivos, diseño e implementación de Tablas de Retención Documental (TRD), digitalización e indexación de documentos, y asesoría especializada en administración documental.",
            },
            {
                "title": "Digitalización y Gestión de Información Administrativa y Financiera",
                "text": "Organización, digitalización y gestión eficiente de información y documentos administrativos y financieros.",
            },
        ],
    },
    {
        "slug": "legal-administrativo",
        "title": "Asesoría Administrativa, Legal e Inmobiliaria",
        "icon": "bi-briefcase-fill",
        "summary": "Acompañamiento especializado en procesos administrativos, legales e inmobiliarios.",
        "services": [
            {
                "title": "Asesoría Administrativa y Legal",
                "text": "Acompañamiento especializado para la gestión de procesos administrativos y asuntos legales de la organización.",
            },
            {
                "title": "Consultoría Empresarial",
                "text": "Orientación y acompañamiento estratégico para optimizar procesos, resolver necesidades y fortalecer la gestión organizacional.",
            },
            {
                "title": "Gestión de Trámites Judiciales y Extrajudiciales",
                "text": "Acompañamiento en la gestión y seguimiento de trámites y actuaciones judiciales y extrajudiciales.",
            },
            {
                "title": "Gestión y Asesoría Jurídica Inmobiliaria",
                "text": "Estudios de títulos, elaboración y revisión de minutas de compraventa e hipoteca, y acompañamiento en la formalización y firma de escrituras públicas.",
            },
            {
                "title": "Gestión de Trámites y Servicios Complementarios",
                "text": "Gestión, radicación y seguimiento de trámites ante entidades y organismos competentes, con atención integral y adaptada a cada cliente.",
            },
        ],
    },
    {
        "slug": "gestion-comercial",
        "title": "Gestión Comercial",
        "icon": "bi-graph-up",
        "summary": "Estrategias para fortalecer la relación con tus clientes y mejorar el flujo de caja.",
        "services": [
            {
                "title": "Fidelización y Recuperación de Clientes",
                "text": "Estrategias para fortalecer la relación con los clientes, incrementar su permanencia y recuperar clientes inactivos o en riesgo de desvinculación.",
            },
            {
                "title": "Gestión y Recaudo de Cartera",
                "text": "Apoyo especializado en la gestión, seguimiento y recaudo de cartera, con estrategias de contacto y cobranza para mejorar los niveles de recuperación.",
            },
        ],
    },
    {
        "slug": "tecnologia-audiovisual",
        "title": "Tecnología y Comunicación Visual",
        "icon": "bi-camera-reels",
        "summary": "Soporte a tus aplicativos y producción audiovisual de alta calidad para tu marca.",
        "services": [
            {
                "title": "Asistencia y Soporte Aplicativo Software",
                "text": "Soporte multicanal, resolución de incidencias, mantenimiento preventivo, monitoreo constante y capacitación técnica para garantizar la continuidad operativa de tus herramientas tecnológicas.",
            },
            {
                "title": "Servicios Audiovisuales y Fotográficos Integrales",
                "text": "Producción técnica de audio, video e iluminación, fotografía corporativa, edición y postproducción, y consultoría creativa para potenciar la comunicación visual de tu organización.",
            },
        ],
    },
]

# Vista plana de todos los servicios (útil para contadores / formulario de contacto)
ALL_SERVICES = [s["title"] for cat in SERVICE_CATEGORIES for s in cat["services"]]

STATS = [
    {"number": "20+", "label": "Servicios especializados"},
    {"number": "6-18", "label": "Años de experiencia del equipo"},
    {"number": "2", "label": "Grandes compañías atendidas"},
    {"number": "100%", "label": "Confidencialidad garantizada"},
]

# --- Galería del equipo ----------------------------------------------------
# Fotos reales del equipo de RO en sus puestos de trabajo. Los archivos viven
# en app/static/img/gallery/. Se muestran de forma aleatoria en la home.
GALLERY_IMAGES = [
    "gallery-01.jpg",
    "gallery-02.jpg",
    "gallery-03.jpg",
    "gallery-04.jpg",
    "gallery-05.jpg",
    "gallery-06.jpg",
    "gallery-07.jpg",
    "gallery-08.jpg",
    "gallery-09.jpg",
    "gallery-10.jpg",
    "gallery-11.jpg",
    "gallery-12.jpg",
]

# Foto principal del hero (equipo completo de RO)
HERO_IMAGE = "hero/team-hero.jpg"
