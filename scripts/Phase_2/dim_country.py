import pandas as pd
from . import csv_utils as utils

df: pd.DataFrame = None


def clean_data():
    global df
    raw_data = pd.read_csv(f"./csv_data/raw/country.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Code"])  # sort table by series code
    df.reset_index(drop=True, inplace=True)


def get_df(transpose: bool = False) -> pd.DataFrame:
    """Returns pandas dataframe of country dimension table (clean)"""
    global df
    if df is None:
        clean_data()  # init clean data & assign to global df
    return df.T if transpose else df  # return transpose table or not


def get_csv(index: bool = False):
    utils.get_csv(get_df(), "dim_country.csv", index=index)
