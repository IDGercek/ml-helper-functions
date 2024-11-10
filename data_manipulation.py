import pandas as pd

def normalize(x):
    """
        Normalizes a Pandas DataFrame using mean normalization.
        This object should have .mean() and .std() functions available.
    """
    return (x-x.mean())/x.std()

def revert_normalization(x):
    """
        Reverts the normalization operation applied to an object.
        This object should have .mean() and .std() functions available.
    """
    return (x * x.std()) / x.mean()