import pandas as pd
from . import csv_utils as utils

df: pd.DataFrame = None
index_label = "Series Code"


def clean_data():
    """Perform data cleaning on countries' raw data and assign to global dataframe df"""
    frames = []  # store different country's data frame
    for i in range(len(utils.countries)):  # for each country
        raw_data = pd.read_csv(f"./csv_data/raw/country/{utils.country_codes[i]}.csv")  # reading raw csv data

        clean_data = raw_data.sort_values(by=["Country Code"])  # sort table by series code

        # clean up year's cols name
        clean_data.rename(columns=lambda n: n.split(' ')[0] if (n[5] == "[") else n, inplace=True)
        drop_cols = ["Country Name", "Country Code", "Scale (Precision)", "Series Name", "1990"]

        # drop unused cols
        clean_data.drop(columns=drop_cols, inplace=True)

        # append country name & code to current country
        clean_data.loc[-2] = ["C.NAME"] + [utils.countries[i]] * 3
        clean_data.loc[-1] = ["C.CODE"] + [utils.country_codes[i]] * 3
        clean_data.index = clean_data.index + 2

        # reset table indexes
        clean_data.sort_index(inplace=True)
        clean_data.set_index(index_label, inplace=True)
        frames.append(clean_data)
    global df  # modify global df
    df = pd.concat(frames, axis=1)  # concat all countries' data frames
    df.dropna(inplace=True)  # drop NaN values


def get_df(transpose: bool = True) -> pd.DataFrame:
    """Returns pandas dataframe of country dimension table (clean)"""
    global df
    if df is None:
        clean_data()  # init clean data & assign to global df
    if transpose:
        # return transpose table
        return df.T.reset_index().rename(columns={"index": "Decades"}).astype({'Decades': 'int64'})
    else:
        return df


def get_csv(index: bool = True):
    # export dataframe df as .csv file in ../csv_data/ folder
    utils.get_csv(get_df(), "dim_country.csv", index=index, index_label=index_label)
