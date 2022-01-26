#!bin/bash

pip install -r requirements.txt
pip install dvc
cd src
python get_data.py
cd ..
dvc repro
jupyter-lab analysis.ipynb
