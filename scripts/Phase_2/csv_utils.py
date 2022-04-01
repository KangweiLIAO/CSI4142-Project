import os
import pandas as pd

countries = ["Canada", "China", "India", "Liberia", "Mexico", "Mozambique",
             "United States", "Vietnam", "South Africa"]

country_codes = ["CAN", "CHN", "IND", "LBR", "MEX", "MOZ", "USA", "VNM", "ZAF"]

yearly_data = ["education", "event", "health", "life_quality", "population"]


def get_csv(data: pd.DataFrame, filename: str, index: bool, index_label=None, save_path="csv_data/"):
    """Export csv data with default settings"""
    if not os.path.isdir("csv_data"):
        os.mkdir(os.getcwd() + "/csv_data")
    data.to_csv(path_or_buf=save_path+filename, index=index, index_label=index_label)
