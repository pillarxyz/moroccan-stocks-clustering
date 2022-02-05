from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd
import json
import datetime
import os


with open("isin_code.json") as f:
    isin_code = json.load(f)
    f.close()

isin_code = json.loads(isin_code)

tickers = [item['name'] for item in isin_code]

def get_code(name):
    for ticker in isin_code :
        if ticker["name"] == name :
            code = ticker['ISIN']
            return code


def get_data(soup):
    table = json.loads(soup.text.encode().decode('utf-8-sig'))
    row_data = pd.DataFrame(table["result"])
    date = row_data['date']
    row_data.drop(['date'],axis=1,inplace=True)
    row_data.index = date
    row_data.columns = ["Value","Low","High","Variation (%)","Volume"]
    return row_data



def get_masi(soup):
    table = json.loads(soup.text.encode().decode('utf-8-sig'))
    row_data = pd.DataFrame(table["result"])
    date = row_data['labels']
    row_data.drop(['labels'],axis = 1, inplace = True)
    row_data.index = date
    row_data.columns = ["MASI"]
    return row_data


def produce_data(data, start, end):
    start = pd.to_datetime(start).date()
    end = pd.to_datetime(end).date()
    return data.loc[start:end]


def loadata(name, start = None, end = None):
	code = get_code(name)
	if name != "MASI":
		if start and end:
			link = f"https://www.leboursier.ma/api?method=getPriceHistory&ISIN={code}&format=json&from={start}&to=(end)"
		else :
			start = '2011-09-18'
			end = str(datetime.datetime.today().date())
			link = f"https://www.leboursier.ma/api?method=getPriceHistory&ISIN={code}&format=json&from={start}&to={end}"

		request_data = requests.get(link)
		soup = bs(request_data.text,features="lxml")
		data=get_data(soup)
	else:
		link = "https://www.leboursier.ma/api?method=getMasiHistory&periode=10y&format=json"
		request_data = requests.get(link)
		soup = bs(request_data.text,features="lxml")
		data_all = get_masi(soup)
		if start and end :
			data = produce_data(data_all,start,end)
		else:
			data = data_all
	return data



def loadmany(*args, start=None, end=None):
	data = []
	for i in args:
		provisoir = loadata(i,start,end)
		row = provisoir["Value"]
		data.append(row)

	data = pd.concat(data, axis = 1, sort = False).reindex(data[0].index)
	data.columns = args
	return data

if __name__ == "__main__":
    stock_ticker = tickers
    stock_ticker.remove('MASI')

    stocks_df = loadmany(*stock_ticker)
    
    masi = loadata('MASI')
    stocks_df["MASI"] = masi.values

    if not os.path.isdir("../data"):
        os.mkdir("../data")
    
    stocks_df.to_csv("../data/stocks.csv")
