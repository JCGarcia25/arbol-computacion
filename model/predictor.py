import pandas as pd
from utils.cleaner import limpiar_y_transformar

def predecir_desde_datos(df_crudo: pd.DataFrame, modelo):
    # Aplicar limpieza y transformaciones
    df_transformado = limpiar_y_transformar(df_crudo)

    # Asegurar que las columnas coincidan con las usadas durante el entrenamiento
    columnas_modelo = modelo.feature_names_in_
    for col in columnas_modelo:
        if col not in df_transformado.columns:
            df_transformado[col] = 0
    df_transformado = df_transformado[columnas_modelo]

    # Realizar predicción
    pred = modelo.predict(df_transformado)
    return pred[0]