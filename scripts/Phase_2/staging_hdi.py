import pandas as pd
from . import utils_csv as utils


def clean_data():
    raw_data = pd.read_csv("./csv_data/raw/HDI.csv")  # reading raw csv data
    df = raw_data.sort_values(by=["Country Code"])  # sort table by country code
    df.drop(df[df["Country Code"].map(lambda x: x not in utils.country_codes)].index, inplace=True)
    df.drop(df[df["Year"].map(lambda x: x < 2004 or x > 2021)].index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def get_df() -> pd.DataFrame:
    return clean_data()


def get_csv():
    utils.get_csv(get_df(), "hdi.csv", index=True, index_label="hdi_id")


def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    get_df().to_sql("staging_hdi", con=engine, method='multi', if_exists=if_exists,
                    index=True, index_label="hdi_id", dtype=dtype)
