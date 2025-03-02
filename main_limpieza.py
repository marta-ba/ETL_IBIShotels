import pandas as pd
import numpy as np
import seaborn as sns
from src.soporte_limpieza import tranform_dates
import os


def clean_data(archivo_entrada, archivo_salida):
    """Limpia y transforma un archivo CSV con datos de hoteles
    
    Procesos realizados:
    - Carga el archivo CSV en un DataFrame de pandas.
    - Convierte las columnas de fecha a formato datatime.
    -
    Args:
        archivo_entrada (_str_): The path to the CSV file to be cleaned.
        archivo_salida (_str_): The path to save the cleaned CSV file.

    Returns:
        None. Save the cleaned CSV file in the specified path.
    
    Exceptions:
        - Show a message if the file is not found.
        - Avoids errors if any of the columns are not found.
    """
    df = pd.read_csv(archivo_entrada)
    df['date'] = df['date'].apply(tranform_dates)
    df.to_csv(archivo_salida, index=False)