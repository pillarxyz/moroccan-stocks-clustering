import tslearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tslearn.clustering import TimeSeriesKMeans, silhouette_score
from tslearn import metrics
import os
import json
import joblib

km_metrics = {}

n_clusters = 4
seed = 42
metric = 'dtw'

np.random.seed(seed)

# Loading processed dataset
stocks = pd.read_csv("data/processed_df.csv").drop('date', axis = 1)
ts = np.loadtxt("data/data_preprocessed.csv")
ts = ts.reshape(ts.shape[0], ts.shape[1], 1)
cols = stocks.columns

# Defining and training K-means
km = TimeSeriesKMeans(n_clusters = n_clusters, random_state = seed, metric = metric)
y_pred = km.fit_predict(ts)

# Saving metrics
s = silhouette_score(ts, y_pred, metric = metric)
inertia = km.inertia_

km_metrics['Number of Clusters'] = n_clusters
km_metrics['Silhouette Score'] = s
km_metrics['Inertia'] = inertia

if not os.path.isdir("model"):
    os.mkdir("model")
    
# Saving models
joblib.dump(km, "model/kmeans.sav")

with open('model/metrics.json', 'w') as f:
    json.dump(km_metrics, f)

# Cluster distribution
clusters_df = pd.DataFrame({'Company\'s stock':stocks.columns, 'Cluster': y_pred}).sort_values(by = 'Cluster')

if not os.path.isdir("plots"):
    os.mkdir("plots")
    
cluster_c = clusters_df["Cluster"].value_counts().sort_index()
cluster_n = [f"Cluster{str(i)}" for i in range(km.n_clusters)]
fig, ax = plt.subplots(1, 1,figsize=(15,5))
ax.set_title("Cluster Distribution for KMeans")
ax.bar(cluster_n, cluster_c)
plt.savefig('plots/cdistribution.jpeg')

# Visualize clustered time series
colors = ['b', 'g','r', 'k', 'orange', 'brown', 'y']
fig, ax = plt.subplots(10, 7,figsize=(35,35))
for i in range(10):
    for j in range(7):
        try:
            ax[i, j].plot(stocks[cols[i*7+j]].values, color = colors[y_pred[i*7+j]])
            ax[i, j].set_title(f"{cols[i*7+j]}, Cluster {y_pred[i*7+j]}")
        except Exception as e:
            fig.delaxes(ax[i, j])
            continue
plt.savefig('plots/clustered_timeseries.jpeg')
