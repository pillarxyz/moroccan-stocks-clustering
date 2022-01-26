#!bin/bash

pip install -r requirements.txt
dvc repro
jupyter-lab analysis.ipynb
