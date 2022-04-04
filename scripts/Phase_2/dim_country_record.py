import pandas as pd
from . import utils_csv as utils


def clean_data() -> pd.DataFrame:
    """Perform data cleaning on raw data and return it"""
    df: pd.DataFrame = None
    frames = []  # store different country's data frame
    for i in range(len(utils.countries)):  # for each country
        raw_data = pd.read_csv(f"./csv_data/raw/country/{utils.country_codes[i]}.csv")  # reading raw csv data
        temp = raw_data.sort_values(by=["Series Code"])  # sort table by series code
        # clean up year's cols name
        temp.rename(columns=lambda n: n.split(' ')[0] if (n[5] == "[") else n, inplace=True)
        drop_cols = ["Country Name", "Country Code", "Scale (Precision)", "Series Name", "1990"]

        # drop unused cols
        temp.drop(columns=drop_cols, inplace=True)

        # append country name & code to current country
        temp.loc[-2] = ["Country Name"] + [utils.countries[i]] * 3
        temp.loc[-1] = ["Country Code"] + [utils.country_codes[i]] * 3
        temp.index = temp.index + 2

        # reset table indexes
        temp.sort_index(inplace=True)
        temp.set_index("Series Code", drop=True, inplace=True)
        frames.append(temp)
    df = pd.concat(frames, axis=1)  # concat all countries' data frames
    df.dropna(inplace=True)  # drop NaN values
    return df


def get_df() -> pd.DataFrame:
    """Returns transformed pandas dataframe of country record dimension table (clean)"""
    frame = clean_data()
    return frame.T.reset_index().rename(columns={"index": "Decades"}).astype({'Decades': 'int64'})


def export_csv(index: bool = False):
    """Export the dataframe as a csv file in ../csv_data/ folder"""
    frame = get_df()
    utils.get_csv(frame, "dim_country_record.csv", index=index, index_label="record_id")


def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    frame = get_df()
    frame.to_sql("dim_country_record", con=engine, method='multi', if_exists=if_exists,
                 index=True, index_label="record_id", dtype=dtype)
