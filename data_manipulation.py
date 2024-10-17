import pandas as pd

def normalize_dataframe(df: pd.DataFrame):
    """
        Normalizes a Pandas DataFrame using mean normalization.
    """
    return (df-df.mean())/df.std()

def normalize_dataframe_column(col: pd.Series):
    """
        Normalizes a Pandas DataFrame column using mean normalization.
    """
    return (col-col.mean())/col.std()