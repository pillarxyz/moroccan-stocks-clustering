#!bin/bash

pip3 install -r requirements.txt
pip3 install dvc
cd src
python get_data.py
cd ..
dvc repro
