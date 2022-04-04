import pandas as pd
from time import strptime
from . import csv_utils as utils

df: pd.DataFrame = None


def clean_data():
    global df
    raw_data = pd.read_csv("./csv_data/raw/event.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Country Code"])  # sort table by country code
    df.reset_index(drop=True, inplace=True)
    df["Start Date"] = df["Start Date"].apply(lambda x: int(x[0]) if not x[1].isdigit() else int(x[:2]))
    df["End Date"] = df["End Date"].apply(lambda x: int(x[0]) if not x[1].isdigit() else int(x[:2]))
    df["Start Month"] = df["Start Month"].apply(lambda x: strptime(x, "%B").tm_mon)
    df["End Month"] = df["End Month"].apply(lambda x: strptime(x, "%B").tm_mon)


def get_df(transpose: bool = False) -> pd.DataFrame:
    """Returns pandas dataframe of country dimension table (clean)"""
    global df
    if df is None:
        clean_data()  # init clean data & assign to global df
    return df.T if transpose else df  # return transpose table or not


def get_csv(index: bool = True):
    utils.get_csv(get_df(), "dim_event.csv", index=index, index_label="event_id")
