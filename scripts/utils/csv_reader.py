import os, csv
import pandas as pd

countries = ["China", "Canada", "Mexico", "Mozambique", "India",
             "United States", "Vietnam", "Liberia", "South Africa"]

def extract_csv(file_path):
    rows = []
    file_path = os.getcwd() + file_path  # file path relative to project root
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', escapechar="'")
        for row in reader:
            rows += [row]
    return rows

# def generate_sql(rows, data_type):
#     result = []
#     if (data_type in ['health', 'population', 'education']):
#         for i in range(len(rows[0])):
#             if (i > 0) and (rows[0][i] not in result):
#                 temp = '\"' + str(rows[0][i]) + '\" numeric,'
#                 if (temp not in result):
#                     result.append(temp)
#     print(' '.join(result))