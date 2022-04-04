import pandas as pd
from . import utils_csv as utils


def init(start="2005", end="2021"):
    """Generate month dimension table within [start,end)"""
    df = pd.DataFrame({"Date": pd.date_range(start, end, freq="M")})
    df["Month"] = df.Date.dt.month
    df["Year"] = df.Date.dt.year
    df["Decades"] = df.Date.dt.year - df.Date.dt.year % 10
    df.drop(columns=["Date"], inplace=True)
    return df


def get_df() -> pd.DataFrame:
    return init()


def get_csv():
    utils.get_csv(get_df(), "dim_date.csv", index=True)


def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    get_df().to_sql("dim_date", con=engine, method='multi', if_exists=if_exists,
                    index=True, index_label="date_id", dtype=dtype)
