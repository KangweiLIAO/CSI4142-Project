import numpy as np
import pandas as pd
from . import utils_csv as utils


def clean_data() -> list[pd.DataFrame]:
    """Perform data cleaning on raw data and return it"""
    dfs: list[pd.DataFrame] = []
    for i in range(len(utils.yearly_data)):
        raw_data = pd.read_csv(f"./csv_data/raw/{utils.yearly_data[i]}.csv")
        clean_df = raw_data.sort_values(by=["Country Code"])
        clean_df.rename(columns=lambda n: n.split(' ')[0] if (n[5] == "[") else n, inplace=True)
        clean_df.replace('..', np.nan, inplace=True)

        rows_per_country = clean_df["Country Code"].to_list().index(utils.country_codes[1])
        drop_cols = ["Country Name", "Country Code", "Series Name"]
        clean_df.drop(columns=drop_cols, inplace=True)

        frames = []
        for c in range(len(utils.country_codes)):
            # insert country name/code into each temp frame
            temp = clean_df.iloc[c*rows_per_country:c*rows_per_country+rows_per_country, :].copy()
            temp.loc[-2] = ["Country Name"] + [utils.countries[c]] * 16
            temp.loc[-1] = ["Country Code"] + [utils.country_codes[c]] * 16
            temp.index = temp.index + 2
            temp.sort_index(inplace=True)
            temp.set_index("Series Code", inplace=True)
            frames.append(temp)
        dfs.append(pd.concat(frames, axis=1))
    return dfs


def get_dfs() -> pd.DataFrame:
    """Returns transformed pandas dataframes table (clean)"""
    frames = [df.T.reset_index().rename(columns={"index": "Years"}) for df in clean_data()]
    for df in frames:
        # Parse corresponding columns' type
        df[df.columns[0]] = df[df.columns[0]].astype('int64')
        df[df.columns[3:]] = df[df.columns[3:]].astype('float64')
    return frames


def get_csv():
    """Export the dataframes as a csv file in ../csv_data/ folder"""
    frames = get_dfs()
    for i in range(len(frames)):
        utils.get_csv(frames[i], f"dim_{utils.yearly_data[i]}.csv",
                      index=True, index_label=f"{utils.yearly_data[i]}_id")


def push(engine, if_exists='replace', dtype=None):
    """Push this dimension to the database"""
    frames = get_dfs()
    for i in range(len(frames)):
        frames[i].to_sql(
            f"dim_{utils.yearly_data[i]}", con=engine, method='multi', if_exists=if_exists,
            index_label=f"{utils.yearly_data[i]}_id", dtype=dtype)
