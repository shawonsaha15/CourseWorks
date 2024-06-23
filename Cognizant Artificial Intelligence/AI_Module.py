# -*- coding: utf-8 -*-
"""AI Module.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UECS_MOGoMCUBV_x1K60AyKTZJkhJN_p
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Load the data
def load_data(path: str = "/path_to_csv"):
  """
  This function takes a path to CSV file as a string and loads into a Pandas
  Dataframe
  :param    path: str, relative path of the CSV file
  :return   df: pd.DataFrame
  """
  df = pd.read_csv(f"{path}")
  df = df.drop(columns=["Umnamed: 0"], inplace=True, errors='ignore')
  return df