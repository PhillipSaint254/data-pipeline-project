import pandas as pd


def get_tables(path):
    data = pd.read_csv(path, sep=":")
    return data.query("to_be_loaded == 'yes'")
