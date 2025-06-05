from .clear_functions import limpiar_texto, clasificar_ocupacion, asignar_categoria, limpiar_texto_multiple, limpiar_titulo, generar_one_hot_por_respuesta, clasificar_titulo, normalizar_texto, corregir_universidad
from data.mappings import *
import pandas as pd

def limpiar_y_transformar(df_crudo: pd.DataFrame) -> pd.DataFrame:

    df_limpio = pd.DataFrame()
    df_onehot_ocupacion = pd.DataFrame()
    df_onehot_campo_desempe = pd.DataFrame()
    df_onehot_competencias = pd.DataFrame()
    df_onehot_titulos = pd.DataFrame()

    df_limpio['sexo'] = df_crudo['sexo'].str.strip().str.lower()

    df_limpio['sexo'] = df_limpio['sexo'].map({'masculino': 1, 'femenino': 0})

    df_limpio['edad'] = df_crudo['edad'].map(edad_orden)

    df_limpio['ocupacion'] = df_crudo['ocupacion'].apply(clasificar_ocupacion)

    df_limpio['ocupacion'].unique()

    df_limpio['ocupacion'] = pd.Categorical(df_limpio['ocupacion'], categories=ocupaciones_fijas, ordered=True)

    df_onehot_ocupacion = pd.get_dummies(df_limpio['ocupacion'], prefix='ocupacion', dtype=int)

    df_limpio['campo'] = df_crudo['campo'].str.strip().str.lower()

    df_limpio['campo'] = df_limpio['campo'].apply(asignar_categoria)

    df_limpio['campo'] = pd.Categorical(df_limpio['campo'], categories=categorias_fijas, ordered=True)

    df_onehot_campo_desempe = pd.get_dummies(df_limpio['campo'], prefix='campo', dtype=int)

    df_limpio['competencias'] = df_crudo['competencias'].apply(limpiar_texto_multiple)

    one_hot_resultado = df_limpio['competencias'].apply(generar_one_hot_por_respuesta)

    df_onehot_competencias = pd.DataFrame(one_hot_resultado.tolist(), columns=categorias_competencias.keys())

    df_limpio['egresado_unillanos'] = df_crudo['egresado_unillanos'].map({'Sí': 1, 'No': 0})

    df_limpio['titulo'] = df_crudo['titulo'].apply(limpiar_titulo)

    df_onehot_titulos['titulo'] = df_limpio['titulo'].apply(clasificar_titulo)

    df_onehot_titulos = pd.get_dummies(df_onehot_titulos['titulo'], prefix='titulo', dtype=int)

    df_limpio['universidad_titulo']= df_crudo['universidad_titulo'].apply(limpiar_texto)

    df_limpio['universidad_titulo'] = df_limpio['universidad_titulo'].apply(corregir_universidad)

    df_limpio['universidad_titulo'] = df_limpio['universidad_titulo'].apply(limpiar_texto)

    df_limpio['universidad_titulo'] = df_limpio['universidad_titulo'].map(universidad_titulo_tipo)

    df_limpio['porcentaje_virtualidad'] = df_crudo['porcentaje_virtualidad'].map(map_porcentaje_virtual)

    # Crear DataFrame base con columnas simples
    df_modelo = pd.DataFrame()
    df_modelo['sexo'] = df_limpio['sexo']
    df_modelo['edad'] = df_limpio['edad']
    df_modelo['egresado_unillanos'] = df_limpio['egresado_unillanos']
    df_modelo['universidad_titulo'] = df_limpio['universidad_titulo'].map({'publica': 0, 'privada': 1})
    df_modelo['porcentaje_virtualidad'] = df_limpio['porcentaje_virtualidad']

    # Concatenar columnas one-hot al DataFrame base
    df_modelo = pd.concat([
        df_modelo,
        df_onehot_ocupacion,
        df_onehot_campo_desempe,
        df_onehot_competencias,
        df_onehot_titulos
    ], axis=1)

    print(df_modelo)

    return df_modelo