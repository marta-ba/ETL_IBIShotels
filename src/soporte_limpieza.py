import pandas as pd
def tranform_dates(dataframe, col_list):
    """Transforms a list of columns to datetime format.
    
    Args:
        dataframe (pd.DataFrame_): The DataFrame to be transformed.
        col_list (_list_): A list of columns to be transformed.
    
    Returns:
        None. Transforms the columns in the DataFrame to datetime format.
    """
    for col in col_list:
        if col in dataframe.columns:
            dataframe[col] = pd.to_datetime(dataframe[col], errors='coerce')
        else:
            print(f'Column {col} not found in the DataFrame
    return dataframe
                
                  