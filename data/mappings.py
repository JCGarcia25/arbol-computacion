edad_orden = {
    'Menor de 20 años': 0,
    '21 a 25 años': 1,
    '26 a 30 años': 2,
    '31 a 35 años': 3,
    '36 a 40 años': 4,
    '41 a 45 años': 5,
    'Mayor a 45 años': 6
}

desarrollo_software = ['desarrollador', 'developer', 'devops', 'qa', 'fullstack', 'backend', 'frontend',
 'swe', 'programador', 'analista qa', 'scrum', 'tester', 'web', 'ingeniero de software',
 'software engineer', 'arquitecto software', 'movil', 'backend', 'frontend']

ingenieria_sistemas = ['sistemas', 'tecnologia', 'soporte', 'infraestructura', 'seguridad informatica',
 'ciberseguridad', 'director de sistemas', 'coordinador de tecnologia', 'servidores',
 'bases de datos', 'profesional ti', 'networking', 'telecomunicaciones','analista de datos']

ingenieria_electrica = ['electricista', 'electrico', 'electrica', 'electrónica', 'subestaciones',
 'alta tension', 'potencia', 'residente electrico', 'técnico electricista',
 'ingeniero electricista', 'diseño electrico', 'baja tension', 'iluminacion']

ingenieria_civil = ['civil', 'residente obra', 'director obra', 'supervisor obra', 'construcción',
 'postventas', 'estructural', 'diseño estructural', 'civiles', 'arquitecto',
 'coordinador obra', 'planos', 'ingeniero civil']

ingenieria_mecanica = ['mecanico', 'mantenimiento', 'supervisor mantenimiento', 'producción',
 'confiabilidad', 'electromecanico', 'jefe de producción', 'técnico mantenimiento',
 'cda', 'taller', 'mecanica', 'operación y mantenimiento']

ingenieria_industrial = ['industrial', 'proyectos', 'logistica', 'mejoramiento', 'gestor', 'gestión',
 'interventoría', 'consultor dnp', 'coordinador de operaciones', 'planeación',
 'planificación', 'oficina técnica', 'procesos']

ingenieria_ambiental = ['ambiental', 'agronomo', 'lider ambiental', 'coordinador ambiental',
 'impacto ambiental', 'ingeniero ambiental', 'compensaciones', 'forestal',
 'ecología', 'avicultura']

educacion = ['docente', 'profesor', 'universitario', 'instructor', 'formador', 'educador',
 'coordinador académico', 'educación', 'mentor', 'catedrático']

salud = ['medico', 'enfermero', 'salud', 'bienestar', 'biomedico', 'hospital', 'general']

estudiante = ['estudiante','universitario', 'pensionado', 'egresado', 'practica', 'tesista']

independientes = ['independiente', 'freelance', 'consultor', 'contratista', 'cps', 'autonomo',
 'outsourcing', 'asesor externo', 'servicios profesionales', 'comerciante']

administrativas = ['contador', 'administrativo', 'oficina', 'hseq', 'recursos humanos',
 'auxiliar', 'secretario', 'asistente', 'logística', 'gestión documental',
 'gerente comercial', 'analista facturación', 'control interno']

otros =['pensionado']

palabras_clave = {
    'Desarrollo de Software': desarrollo_software,
    'Ingeniería de Sistemas/TI': ingenieria_sistemas,
    'Ingeniería Eléctrica/Electrónica': ingenieria_electrica,
    'Ingeniería Civil/Infraestructura' : ingenieria_civil,
    'Ingeniería Mecánica/Mantenimiento': ingenieria_mecanica,
    'Ingeniería Industrial/Proyectos': ingenieria_industrial,
    'Ingeniería Ambiental/Agro': ingenieria_ambiental,
    'Educación/Formación': educacion,
    'Salud': salud,
    'Estudiantes': estudiante,
    'Independientes/Contratistas': independientes,
    'Administrativas': administrativas,
    'Otros': otros
}

ocupaciones_fijas = [
    "Desarrollo de Software",
    "Ingeniería de Sistemas/TI",
    "Ingeniería Eléctrica/Electrónica",
    "Ingeniería Civil/Infraestructura",
    "Ingeniería Mecánica/Mantenimiento",
    "Ingeniería Industrial/Proyectos",
    "Ingeniería Ambiental/Agro",
    "Educación/Formación",
    "Salud",
    "Estudiantes",
    "Independientes/Contratistas",
    "Administrativas",
    "Otros"
]

categorias_fijas = [
    "Educación",
    "Artes y humanidades",
    "Ciencias sociales, periodismo e información",
    "Administración de empresas y derecho",
    "Ciencias naturales, matemáticas y estadística",
    "Tecnologías de la información y la comunicación",
    "Ingeniería, industria y construcción",
    "Agricultura, silvicultura, pesca y veterinaria",
    "Salud y bienestar",
    "Servicios",
    "Otra"
]

mapeo_personalizado = {
    'programador': 'Tecnologías de la información y la comunicación',
    'cps sistemas en la alcaldia de villavicencio': 'Administración de empresas y derecho',
    'devops engineer': 'Tecnologías de la información y la comunicación',
    'comerciante ferretería y transporte': 'Servicios',
    'asesor control interno': 'Administración de empresas y derecho',
    'comisiónamiento en instrumentación': 'Ingeniería, industria y construcción',
    'logística internacional': 'Administración de empresas y derecho',
    'sst': 'Salud y bienestar',
    'mentor pensamiento computacional': 'Educación',
    'director técnico en cda': 'Servicios'
}

categorias_competencias = {
    'analisis_datos': ['analisis de datos', 'big data', 'estadistica', 'data science', 'analisis'],
    'automatizacion': ['automatizacion', 'control', 'instrumentacion', 'procesos industriales'],
    'energias_limpias': ['energia limpia', 'energias renovables', 'sostenibilidad', 'carbono'],
    'gestion_proyectos': ['gestion de proyectos', 'liderazgo', 'planificacion', 'gestion', 'proyectos'],
    'inteligencia_artificial': ['inteligencia artificial', 'ia', 'machine learning', 'redes neuronales'],
    'ciberseguridad': ['ciberseguridad', 'seguridad informatica'],
    'arquitectura_software': ['arquitectura de software', 'escalables', 'backend', 'frontend'],
    'cloud': ['nube', 'cloud', 'azure', 'aws', 'cloud computing'],
    'habilidades_blandas': ['comunicacion', 'trabajo en equipo', 'asertiva', 'habilidades blandas'],
    'bioingenieria': ['bioingenieria', 'bioinformatica', 'biomedica'],
    'normatividad': ['normatividad', 'regulacion', 'sismoresistente'],
    'otras': ['construccion', 'diseno de estructuras', 'servicio al cliente', 'talento humano'],
}

diccionario_normalizacion = {
    # corporacion universitaria del meta
    'corporacion universitaria del meta (unimneta)': 'corporacion universitaria del meta',
    'corporacion universitaria del meta unimneta': 'corporacion universitaria del meta',
    'corporacion universitaria del meta unimeta': 'corporacion universitaria del meta',
    'corporacion universitaria del meta (unimeta)': 'corporacion universitaria del meta',
    'unimeta': 'corporacion universitaria del meta',
    'corporacion universitaria del meta': 'corporacion universitaria del meta',
    'universidad del meta': 'corporacion universitaria del meta',

    # Universidad de los Llanos
    'universidad de los llanos': 'universidad de los llanos',
    'unillanos': 'universidad de los llanos',
    'unillanos ucc': 'universidad de los llanos',
    'unillanos <3': 'universidad de los llanos',
    'universida dde los llanos': 'universidad de los llanos',
    'universidad de los lanos': 'universidad de los llanos',

    # Universidad Pedagógica y Tecnológica de Colombia
    'universidad pedagogica tecnologica de colombia': 'Universidad Pedagógica y Tecnológica de Colombia',
    'universidad pedagogica tecnologica de colombia uptc': 'Universidad Pedagógica y Tecnológica de Colombia',
    'uptc': 'Universidad Pedagógica y Tecnológica de Colombia',

    # Universidad Nacional de Colombia
    'universidad nacional de colombia': 'Universidad Nacional de Colombia',
    'universidad nacional': 'Universidad Nacional de Colombia',
    'nacional': 'Universidad Nacional de Colombia',
    'universidad nacional de colombia sede bogota': 'Universidad Nacional de Colombia',

    # Universidad Antonio Nariño
    'universidad antonio narino': 'Universidad Antonio Nariño',
    'antonio narino': 'Universidad Antonio Nariño',

    # Universidad Cooperativa de Colombia
    'universidad cooperativa de colombia': 'Universidad Cooperativa de Colombia',
    'universidad cooperativa de colombia sede villavicencio': 'Universidad Cooperativa de Colombia',
    'universidad copertaiva de colombia': 'Universidad Cooperativa de Colombia',
    'universidad cooperativa': 'Universidad Cooperativa de Colombia',
    'u. cooperativa': 'Universidad Cooperativa de Colombia',
    'ucc': 'Universidad Cooperativa de Colombia',
    'cooperativa de colombia': 'Universidad Cooperativa de Colombia',

    # Universidad Santo Tomás
    'universidad santo tomas': 'Universidad Santo Tomás',
    'universidad santo tomas seccional tunja': 'Universidad Santo Tomás',
    'santo tomas': 'Universidad Santo Tomás',
    'santo tomas bogota': 'Universidad Santo Tomás',
    'usta': 'Universidad Santo Tomás',

    # Universidad del Tolima
    'universidad del tolima': 'Universidad del Tolima',
    'en unitolima': 'Universidad del Tolima',

    # Fundación Universitaria San Martín
    'fundacion universitaria san martin': 'Fundación Universitaria San Martín',

    # Universidad Nacional Abierta y a Distancia
    'universidad nacional abierta a distancia': 'Universidad Nacional Abierta y a Distancia',
    'universidad nacional abierta a distancia unad': 'Universidad Nacional Abierta y a Distancia',
    'unad': 'Universidad Nacional Abierta y a Distancia',

    # Universidad Autónoma de Colombia
    'universidad autonoma': 'Universidad Autónoma de Colombia',
    'autonoma de colombia': 'Universidad Autónoma de Colombia',
    'universidad autonoma de colombia': 'Universidad Autónoma de Colombia',

    # Fundación Universitaria Los Libertadores
    'fundacion universitaria los libertadores': 'Fundación Universitaria Los Libertadores',
    'los libertadores': 'Fundación Universitaria Los Libertadores',

    # Universidad Industrial de Santander
    'universidad industrial de santander': 'Universidad Industrial de Santander',
    'uis': 'Universidad Industrial de Santander',

    # Universidad de Pamplona
    'universidad de pamplona': 'Universidad de Pamplona',

    # Universidad San José
    'universidad san jose': 'Universidad San José',
    'universidad de sanjose': 'Universidad San José',
    'usanjose': 'Universidad San José',
    'san jose': 'Universidad San José',

    # Universidad Francisco de Paula Santander
    'universidad francisco de paula santander': 'Universidad Francisco de Paula Santander',

    # Pontificia Universidad Javeriana
    'pontificia universidad javeriana': 'Pontificia Universidad Javeriana',
    'universidad javeriana': 'Pontificia Universidad Javeriana',
    'javeriana': 'Pontificia Universidad Javeriana',

    # Corporación Universitaria Minuto de Dios (Uniminuto)
    'universidad minuto de dios': 'Corporación Universitaria Minuto de Dios',
    'corporacion universitaria minuto de dios': 'Corporación Universitaria Minuto de Dios',
    'uniminuto': 'Corporación Universitaria Minuto de Dios',

    # Universidad de La Salle
    'universidad de la salle': 'Universidad de La Salle',

    # Escuela Tecnológica Instituto Técnico Central
    'escuela tecnologica instituto tecnico central': 'Escuela Tecnológica Instituto Técnico Central',

    # Universidad Piloto de Colombia
    'universidad piloto de colombia': 'Universidad Piloto de Colombia',

    # Escuela Colombiana de Ingeniería Julio Garavito
    'escuela colombiana de ingenieria julio garavito': 'Escuela Colombiana de Ingeniería Julio Garavito',
    'escuela colombiana de ingenieria': 'Escuela Colombiana de Ingeniería Julio Garavito',

    # Politécnico Grancolombiano
    'politecnico grancolombiano': 'Politécnico Grancolombiano',
    'politecnico': 'Politécnico Grancolombiano',

    # Universidad Católica de Colombia
    'universidad catolica de colombia': 'Universidad Católica de Colombia',
    'ucr unir': 'Universidad de costa rica Universidad internacional de la Rioja',

    # SENA
    'sena': 'SENA',

    # UNINCCA
    'unincca': 'UNINCCA',

    # Universidad Libre
    'universidad libre': 'Universidad Libre',
    'unilibre': 'Universidad Libre',

    # Universidad de San Buenaventura
    'universidad san buenaventura': 'Universidad de San Buenaventura',
    'universidad de san buenaventura': 'Universidad de San Buenaventura',

    # Universidad Jorge Tadeo Lozano
    'universidad jorge tadeo lozano': 'Universidad Jorge Tadeo Lozano',
    'jorge tadeo lozano': 'Universidad Jorge Tadeo Lozano',

    # Universidad Nacional Abierta de Venezuela
    'universidad nacional abierta de venezuela': 'Universidad Nacional Abierta de Venezuela',

    # Universidad Distrital Francisco José de Caldas
    'universidad distrital francisco jose de caldas': 'Universidad Distrital Francisco José de Caldas',
    'universidad distrital de bogota': 'Universidad Distrital Francisco José de Caldas',

    # Corporación Universitaria UCOMPENSAR
    'corporacion universitaria ucompensar': 'Corporación Universitaria UCOMPENSAR',

    # Universidad Militar Nueva Granada
    'universidad militar nueva granada': 'Universidad Militar Nueva Granada',

    # Universidad ECCI
    'universidad ecci': 'Universidad ECCI',

    # Corporación Tecnológica Industrial de Colombia (TEINCO)
    'corporacion tecnologica industrial de colombia': 'Corporación Tecnológica Industrial de Colombia',
    'teinco': 'Corporación Tecnológica Industrial de Colombia',

    # Universidad Rafael Belloso Chacín
    'universidad rafael belloso chacin': 'Universidad Rafael Belloso Chacín',

    # Colegio Mayor de Cundinamarca
    'colegio mayor de cundinamarca': 'Colegio Mayor de Cundinamarca',

    # Fundación Universitaria Juan de Castellanos
    'fundacion universitaria juan de castellanos': 'Fundación Universitaria Juan de Castellanos',

    # Corporación Universitaria UNITEC
    'corporacion universitaria unitec': 'Corporación Universitaria UNITEC',

    # Universidad de Ibagué
    'universidad de ibague': 'Universidad de Ibagué',

    # Universidad del Magdalena
    'universidad del magdalena': 'Universidad del Magdalena',

    # Variante NaN (si aparece como cadena literal)
    'nan': 'no aplica'
}

universidad_titulo_tipo = {
    # Públicas
    "universidad de los llanos": "publica",
    "universidad pedagogica tecnologica de colombia": "publica",
    "universidad nacional de colombia": "publica",
    "universidad del tolima": "publica",
    "universidad nacional abierta a distancia": "publica",
    "universidad industrial de santander": "publica",
    "universidad de pamplona": "publica",
    "universidad francisco de paula santander": "publica",
    "escuela tecnologica instituto tecnico central": "publica",
    "sena": "publica",
    "universidad nacional abierta de venezuela": "publica",
    "universidad distrital francisco jose de caldas": "publica",
    "universidad militar nueva granada": "publica",
    "universidad del magdalena": "publica",

    # Privadas
    "corporacion universitaria del meta": "privada",
    "universidad antonio narino": "privada",
    "universidad cooperativa de colombia": "privada",
    "universidad santo tomas": "privada",
    "fundacion universitaria san martin": "privada",
    "universidad autonoma de colombia": "privada",
    "fundacion universitaria los libertadores": "privada",
    "universidad san jose": "privada",
    "pontificia universidad javeriana": "privada",
    "corporacion universitaria minuto de dios": "privada",
    "universidad de la salle": "privada",
    "universidad piloto de colombia": "privada",
    "escuela colombiana de ingenieria julio garavito": "privada",
    "politecnico grancolombiano": "privada",
    "universidad catolica de colombia": "privada",
    "unincca": "privada",
    "universidad libre": "privada",
    "universidad de san buenaventura": "privada",
    "universidad jorge tadeo lozano": "privada",
    "corporacion universitaria ucompensar": "privada",
    "universidad ecci": "privada",
    "corporacion tecnologica industrial de colombia": "privada",
    "universidad rafael belloso chacin": "privada",
    "colegio mayor de cundinamarca": "privada",
    "fundacion universitaria juan de castellanos": "privada",
    "corporacion universitaria unitec": "privada",
    "universidad de ibague": "privada",
}

interes_orden = {
    'Muy interesado, me inscribiría definitivamente!': 1,
    'Interesado, me podría inscribir': 2,
    'Poco interesado, posiblemente no me inscriba': 3,
    'No me interesa y no me inscribiría': 4,
    'No sabe / No responde': 5
}

interes = {
    'Muy interesado, me inscribiría definitivamente!': 1,
    'Interesado, me podría inscribir': 1,
    'No sabe / No responde': 0,
    'Poco interesado, posiblemente no me inscriba': -1,
    'No me interesa y no me inscribiría': -1,
}

map_porcentaje_virtual = {
    '10%': 10.0,
    '30%': 30.0,
    '50%': 50.0,
    'No debe tener componente de apoyo virtual a la presencialidad': 0.0
}

CLASES_INTERES = {
    -1: "No interesado",
     0: "Neutro",
     1: "Interesado"
}

CLASES_RANGO = {
    1: "2 - 4 SMMLV",
    2: "4 - 6 SMMLV",
    3: "6 - 8 SMMLV",
    4: "8 - 10 SMMLV",
    5: "más de 12 SMMLV",
}