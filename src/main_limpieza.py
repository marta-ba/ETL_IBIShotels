import pandas as pd
import numpy as np  
"""funcion para convertir a formato fecha una lista de columnas de un dataframe
    """
def convertir_a_fecha(df, lista_columnas):
    for col in lista_columnas:
        df[lista_columnas] = pd.to_datetime(df[lista_columnas], errors='coerce')
    return df