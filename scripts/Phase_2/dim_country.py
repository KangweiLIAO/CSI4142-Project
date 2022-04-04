import pandas as pd
from . import utils_csv as utils


def clean_data() -> pd.DataFrame:
    raw_data = pd.read_csv(f"./csv_data/raw/country.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Country Code"])  # sort table by series code
    df.reset_index(drop=True, inplace=True)
    return df


def get_df() -> pd.DataFrame:
    """Returns pandas dataframe of country dimension table (clean)"""
    return clean_data()  # return transpose table or not


def get_csv():
    utils.get_csv(get_df(), "dim_country.csv", index=True, index_label="country_id")


def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    get_df().to_sql("dim_country", con=engine, method='multi', if_exists=if_exists,
                 index=True, index_label="country_id", dtype=dtype)
