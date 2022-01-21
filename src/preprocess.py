import tslearn
import numpy as np
import pandas as pd
from tslearn.preprocessing import TimeSeriesScalerMinMax
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os, argparse

ap = argparse.ArgumentParser()
ap.add_argument("--pca", type = int, choices = [0, 1], required = True, default = 0)
pca = ap.parse_args().pca

stocks_df = pd.read_csv("../data/stocks.csv")

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

if not os.path.isdir("../plots"):
    os.mkdir("../plots")
fig, axs = plt.subplots(10,7,figsize=(35,35))
for i in range(10):
    for j in range(7):
        axs[i, j].plot(stocks_df[cols[i*7+j]].values)
        axs[i, j].set_title(cols[i*7+j])
plt.savefig('../plots/timeseries.jpeg')

# Run PCA (if specified)
def run_pca(data):
    print("running PCA")
    n_components = 40
    pca = PCA(n_components)
    ts_pca = pca.fit_transform(np.array(data).reshape(data.shape[0], data.shape[1]))
    n_pca = pca.n_components_
    most_important = [np.abs(pca.components_[i]).argmax() for i in range(n_pca)]
    initial_feature_names = data.columns
    most_important_names = list(set([initial_feature_names[most_important[i]] for i in range(n_pca)]))
    data_preprocessed = data[most_important_names]
    return data_preprocessed, n_pca, most_important_names

if pca:
    data_preprocessed, n_pca, most_important_names = run_pca(stocks_df)
    data_preprocessed.to_csv("../data/processed_df.csv")
else:
    data_preprocessed = stocks_df
    data_preprocessed.to_csv("../data/processed_df.csv")

# Normalize and reshape time series
ts = np.array(data_preprocessed.T).reshape(data_preprocessed.T.shape[0], data_preprocessed.T.shape[1], 1)
ts = TimeSeriesScalerMinMax().fit_transform(ts)

np.savetxt("../data/data_preprocessed.csv", ts.reshape(ts.shape[0], ts.shape[1]))

