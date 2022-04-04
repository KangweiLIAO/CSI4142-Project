import pandas as pd
from time import strptime
from . import utils_csv as utils


def clean_data():
    raw_data = pd.read_csv("./csv_data/raw/event.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Country Code"])  # sort table by country code
    df.reset_index(drop=True, inplace=True)
    df["Start Date"] = df["Start Date"].apply(lambda x: int(x[0]) if not x[1].isdigit() else int(x[:2]))
    df["End Date"] = df["End Date"].apply(lambda x: int(x[0]) if not x[1].isdigit() else int(x[:2]))
    df["Start Month"] = df["Start Month"].apply(lambda x: strptime(x, "%B").tm_mon)
    df["End Month"] = df["End Month"].apply(lambda x: strptime(x, "%B").tm_mon)
    return df


def get_df() -> pd.DataFrame:
    return clean_data()  # init clean data & assign to global df


def get_csv():
    utils.get_csv(get_df(), "dim_event.csv", index=True, index_label="event_id")

def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    get_df().to_sql("dim_event", con=engine, method='multi', if_exists=if_exists,
                    index=True, index_label="event_id", dtype=dtype)