import numpy as np
import pandas as pd
from . import csv_utils as utils

dfs = []


def clean_data() -> pd.DataFrame:
    global dfs
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
            tmp_df = clean_df.iloc[c*rows_per_country:c*rows_per_country+rows_per_country, :].copy()
            tmp_df.loc[-2] = ["C.NAME"] + [utils.countries[c]] * 16
            tmp_df.loc[-1] = ["C.CODE"] + [utils.country_codes[c]] * 16
            tmp_df.index = tmp_df.index + 2
            tmp_df.sort_index(inplace=True)
            tmp_df.set_index("Series Code", inplace=True)
            frames.append(tmp_df)
        dfs.append(pd.concat(frames, axis=1))


def get_dfs(transpose: bool = True) -> pd.DataFrame:
    global dfs
    if dfs == []:
        clean_data()
    if transpose:
        dfs = [df.T.reset_index().rename(columns={"index": "Year"}) for df in dfs]
    return dfs


def get_csv(index: bool = True):
    for i in range(len(get_dfs())):
        utils.get_csv(dfs[i], f"dim_{utils.yearly_data[i]}.csv", index=index, index_label=f"{utils.yearly_data[i]}_id")
