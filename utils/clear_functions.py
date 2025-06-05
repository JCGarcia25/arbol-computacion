from data.mappings import *
import re
import unicodedata
import pandas as pd
import numpy as np

def limpiar_texto(texto):
    texto = str(texto).lower()                             # pasar a minúsculas
    texto = re.sub(r'[-_/,]', ' ', texto)                  # reemplazar símbolos por espacio
    texto = re.sub(r'\s+y\s+', ' ', texto)           # reemplazar " y " por espacio
    texto = re.sub(r'\s+', ' ', texto).strip()             # quitar espacios extra
    texto = unicodedata.normalize('NFKD', texto)           # quitar acentos
    texto = texto.encode('ASCII', 'ignore').decode('utf-8')
    return texto

def clasificar_ocupacion(texto):
    texto =  limpiar_texto(texto)
    for categoria, keywords in palabras_clave.items():
        for palabra in keywords:
            if palabra in texto:
                return categoria
    return 'Otros'

def asignar_categoria(texto):
    for cat in categorias_fijas:
        if texto == cat.lower():
            return cat
    return mapeo_personalizado.get(texto, "Otra")

def limpiar_texto_multiple(texto):
    texto = str(texto).lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    texto = re.sub(r'[^\w\s,]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def mapear_categoria(frase):
    frase = frase.strip().lower()
    for categoria, palabras in categorias_competencias.items():
        for palabra in palabras:
            if palabra in frase:
                return categoria
    return None

def generar_one_hot_por_respuesta(respuesta):
    frases = str(respuesta).split(',')
    categorias_detectadas = set()

    for frase in frases:
        categoria = mapear_categoria(frase)
        if categoria:
            categorias_detectadas.add(categoria)

    # Ahora generar el one-hot en el orden original
    return [1 if cat in categorias_detectadas else 0 for cat in categorias_competencias.keys()]

def limpiar_titulo(texto):
    texto = str(texto).lower()                             # pasar a minúsculas
    texto = re.sub(r'[-_/,]', ' ', texto)                  # reemplazar símbolos por espacio
    texto = re.sub(r'\s+', ' ', texto).strip()             # quitar espacios extra
    texto = unicodedata.normalize('NFKD', texto)           # quitar acentos
    texto = texto.encode('ASCII', 'ignore').decode('utf-8')
    return texto

def clasificar_titulo(titulo):
    patrones = {
        'ingenieria_electrica': ['electrica', 'electricista'],
        'ingenieria_electronica': ['electronica', 'electronico'],
        'ingenieria_sistemas': ['sistemas', 'informatica', 'software', 'sitemas', 'informatico', 'sistenas','telecomunicaciones'],
        'ingenieria_industrial': ['industrial'],
        'ingenieria_civil': ['civil'],
        'ingenieria_mecanica': ['mecanica', 'mecanico'],
        'ingenieria_quimica': ['quimica', 'quimico'],
        'ingenieria_ambiental': ['ambiental', 'agroindustrial'],
        'economia_administracion': ['economia', 'administracion', 'relaciones internacionales', 'economista', 'empresas', 'administradora'],
        'contador': ['contador', 'publico'],
        'otros_profesionales': ['historiador', 'medico', 'medicina', 'zootecnista', 'geologo', 'arquitecta', 'desarrollador', 'agronomo', 'licenciado'],
        'tecnicos': ['tecnico', 'tecnologia', 'tecnologo'],
        'no_clasificados': ['na', 'n.a', '.', '', 'en curso', 'sí']
    }

    for categoria, palabras_clave in patrones.items():
        for palabra in palabras_clave:
            if palabra in titulo:
                return categoria
    return 'otros_profesionales'

def normalizar_texto(texto):
    if pd.isna(texto):
        return np.nan
    texto = str(texto).lower()
    texto = re.sub(r'\s+', ' ', texto).strip()
    #texto = unidecode.unidecode(texto.lower().strip())
    texto = re.sub(r'\s+', ' ', texto)  # Reemplaza múltiples espacios por uno solo
    return texto

diccionario_normalizacion_normalizado = {
    normalizar_texto(k): v for k, v in diccionario_normalizacion.items()
}

def corregir_universidad(valor):
    if pd.isna(valor):
        return np.nan
    texto_limpio = normalizar_texto(valor)
    # Si está en diccionario, devuelve el nombre oficial
    return diccionario_normalizacion_normalizado.get(texto_limpio, valor.strip().title())