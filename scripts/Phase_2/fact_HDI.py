import pandas as pd
from . import csv_utils as utils

df: pd.DataFrame = None


def clean_data():
    global df
    raw_data = pd.read_csv("./csv_data/raw/HDI.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Country Code"])  # sort table by country code
    df.drop(df[df["Country Code"].map(lambda x: x not in utils.country_codes)].index, inplace=True)
    df.drop(df[df["Year"].map(lambda x: x < 2004 or x > 2021)].index, inplace=True)
    df.reset_index(drop=True, inplace=True)


def get_df() -> pd.DataFrame:
    global df
    if df is None:
        clean_data()
    return df


def get_csv(index: bool = True):
    utils.get_csv(get_df(), "hdi.csv", index=index, index_label="hdi_id")
