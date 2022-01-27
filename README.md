# Moroccan Stocks Clustering

> In progress

## Context

Hey! we don't always have to forecast time series am I right ?

We use k-means to cluster about 70 moroccan stock prices to see their influence on market trends indicated by the MASI (Moroccan All Shares Index) index,
for the case of time series k-means uses DTW (Dynamic Time Warping) metric which is a better indicator for similiarity for time series data

Our analysis leads us to find out about the companies that flourished despite the pandemic, the ones that did suffer but managed to recover and the ones that suffered the most.

## Dependecies

To be able to run the notebook on your machine you need to have [docker installed](https://docs.docker.com/get-docker/)

## Quick Start

To start the notebook and run the pipeline simply run these commands 

```bash
git clone https://github.com/pillarxyz/moroccan-stocks-clustering.git
cd moroccan-stocks-clustering
docker build -t ma_cluster . 
docker run -it -p 8888:8888 ma_cluster
```

## Data Source:

this dataset was scraped from [LeBoursier](https://www.leboursier.ma/)
