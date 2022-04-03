import pandas as pd
from . import csv_utils as utils

df: pd.DataFrame = None


def init_date(start="2005", end="2021"):
    """Generate month dimension table within [start,end)"""
    global df
    df = pd.DataFrame({"Date": pd.date_range(start, end, freq="M")})
    df["Month"] = df.Date.dt.month
    df["Year"] = df.Date.dt.year
    df["Decades"] = df.Date.dt.year - df.Date.dt.year % 10
    df.drop(columns=["Date"], inplace=True)


def get_df() -> pd.DataFrame:
    global df
    if df is None:
        init_date()
    return df


def get_csv(index: bool = True):
    get_df()
    utils.get_csv(df, "dim_date.csv", index=index)
