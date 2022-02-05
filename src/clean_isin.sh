#!/bin/bash

sed -e "s/,\+/,/g" -e "s/,$//" -i ../data/companies_isin.csv
sed -i '1d' ../data/companies_isin.csv
sed -i '2d' ../data/companies_isin.csv
