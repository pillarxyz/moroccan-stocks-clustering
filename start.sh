#!bin/bash

pip install -r requirements.txt
pip install dvc
dvc repro
jupyter-lab analysis.ipynb
