import tslearn
import numpy as np
import pandas as pd
from tslearn.preprocessing import TimeSeriesScalerMinMax
from tslearn.piecewise import PiecewiseAggregateApproximation as PAA
import matplotlib.pyplot as plt
import os, argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("--dimrec", type = int, choices = [0, 1], required = True, default = 0)
dimrec = ap.parse_args().dimrec
n_segments = 10

# Reading data
stocks_df = pd.read_csv("data/stocks.csv")

# Formatting the date column
stocks_df.date = pd.to_datetime(stocks_df.date, format='%d/%m/%Y')

# Dropping column with many missing values
stocks_df.drop(columns = ["SAMIR", "Diac Salaf", "Aradei Capital", "Mutandis", "Immr Invest"], inplace = True)

# Filling other missing values
stocks_df = stocks_df.ffill()
stocks_df = stocks_df.bfill()

# Resample daily data into weekly data
stocks_df = stocks_df.resample('7D', on = 'date').first().reset_index(drop = True)

# setting date as index
stocks_df.index = stocks_df.date
stocks_df.drop("date", axis = 1, inplace = True)

cols = stocks_df.columns

if not os.path.isdir("plots"):
    os.mkdir("plots")

fig, axs = plt.subplots(10,7,figsize=(35,35))
for i in range(10):
    for j in range(7):
        axs[i, j].plot(stocks_df[cols[i*7+j]].values)
        axs[i, j].set_title(cols[i*7+j])
plt.savefig('plots/timeseries.jpeg')

# Normalize and reshape time series
ts = np.array(stocks_df.T).reshape(stocks_df.T.shape[0], stocks_df.T.shape[1], 1)
ts = TimeSeriesScalerMinMax().fit_transform(ts)

# Run PAA (if specified)
def run_paa(ts, n_segments):
    print("running PAA")
    paa = PAA(n_segments = n_segments)
    ts_paa = paa.fit_transform(ts)
    return ts_paa

if dimrec:
    ts = run_paa(ts, n_segments)

stocks_df.to_csv("data/processed_df.csv")
np.savetxt("data/data_preprocessed.csv", ts.reshape(ts.shape[0], ts.shape[1]))

