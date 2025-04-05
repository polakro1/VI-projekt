import pandas as pd
import numpy as np
import talib


def load_data(filepath):
    """
    Load and prepare data from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame with the prepared data.
    """
    data = pd.read_csv(
        filepath,
        sep=";",
        names=["timestamp", "open", "high", "low", "close", "volume"],
        usecols=["timestamp", "open", "high", "low", "close"],
        index_col="timestamp",
        parse_dates=[0],
        date_format="%Y%m%d %H%M%S",
    )
    return data
