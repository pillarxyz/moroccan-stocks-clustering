from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd
import json
import datetime
import os

def notation_code():
      return [{'name': 'Addoha', 'ISIN': 'MA0000011512'},
              {'name': 'AFMA', 'ISIN': 'MA0000012296'},
              {'name': 'Afric Indus', 'ISIN': 'MA0000012114'},
              {'name': 'Afriquia Gaz', 'ISIN': 'MA0000010951'},
              {'name': 'Agma', 'ISIN': 'MA0000010944'},
              {'name': 'Alliances', 'ISIN': 'MA0000011819'},
              {'name': 'Aluminium Maroc', 'ISIN': 'MA0000010936'},
              {'name': 'Aradei Capital', 'ISIN': 'MA0000012460'},
              {'name': 'ATLANTASANAD', 'ISIN': 'MA0000011710'},
              {'name': 'Attijariwafa', 'ISIN': 'MA0000012445'},
              {'name': 'Auto Hall', 'ISIN': 'MA0000010969'},
              {'name': 'Auto Nejma', 'ISIN': 'MA0000011009'},
              {'name': 'BALIMA', 'ISIN': 'MA0000011991'},
              {'name': 'BCP', 'ISIN': 'MA0000011884'},
              {'name': 'BMCI', 'ISIN': 'MA0000010811'},
              {'name': 'Cartier Saada', 'ISIN': 'MA0000011868'},
              {'name': 'CDM', 'ISIN': 'MA0000010381'},
              {'name': 'Central.Danone', 'ISIN': 'MA0000012049'},
              {'name': 'CIH', 'ISIN': 'MA0000011454'},
              {'name': 'Ciments Maroc', 'ISIN': 'MA0000010506'},
              {'name': 'CMT', 'ISIN': 'MA0000011793'},
              {'name': 'Colorado', 'ISIN': 'MA0000011934'},
              {'name': 'COSUMAR', 'ISIN': 'MA0000012247'},
              {'name': 'CTM', 'ISIN': 'MA0000010340'},
              {'name': 'Dari Couspate', 'ISIN': 'MA0000011421'},
              {'name': 'Delattre Lev', 'ISIN': 'MA0000011777'},
              {'name': 'Delta Holding', 'ISIN': 'MA0000011850'},
              {'name': 'Diac Salaf', 'ISIN': 'MA0000010639'},
              {'name': 'DISWAY', 'ISIN': 'MA0000011637'},
              {'name': 'Ennakl', 'ISIN': 'MA0000011942'},
              {'name': 'EQDOM', 'ISIN': 'MA0000010357'},
              {'name': 'FENIE BROSSETTE', 'ISIN': 'MA0000011587'},
              {'name': 'HPS', 'ISIN': 'MA0000011611'},
              {'name': 'IBMaroc', 'ISIN': 'MA0000011132'},
              {'name': 'Immr Invest', 'ISIN': 'MA0000012387'},
              {'name': 'INVOLYS', 'ISIN': 'MA0000011579'},
              {'name': 'Jet Contractors', 'ISIN': 'MA0000012080'},
              {'name': 'LABEL VIE', 'ISIN': 'MA0000011801'},
              {'name': 'LafargeHolcim', 'ISIN': 'MA0000012320'},
              {'name': 'Lesieur Cristal', 'ISIN': 'MA0000012031'},
              {'name': 'Lydec', 'ISIN': 'MA0000011439'},
              {'name': 'M2M Group', 'ISIN': 'MA0000011678'},
              {'name': 'Maghreb Oxygene', 'ISIN': 'MA0000010985'},
              {'name': 'Maghrebail', 'ISIN': 'MA0000011215'},
              {'name': 'Managem', 'ISIN': 'MA0000011058'},
              {'name': 'Maroc Leasing', 'ISIN': 'MA0000010035'},
              {'name': 'Maroc Telecom', 'ISIN': 'MA0000011488'},
              {'name': 'Med Paper', 'ISIN': 'MA0000011447'},
              {'name': 'Microdata', 'ISIN': 'MA0000012163'},
              {'name': 'Mutandis', 'ISIN': 'MA0000012395'},
              {'name': 'Nexans Maroc', 'ISIN': 'MA0000011140'},
              {'name': 'Oulmes', 'ISIN': 'MA0000010415'},
              {'name': 'PROMOPHARM', 'ISIN': 'MA0000011660'},
              {'name': 'Rebab Company', 'ISIN': 'MA0000010993'},
              {'name': 'Res.Dar Saada', 'ISIN': 'MA0000012239'},
              {'name': 'Risma', 'ISIN': 'MA0000011462'},
              {'name': 'S2M', 'ISIN': 'MA0000012106'},
              {'name': 'Saham Assurance', 'ISIN': 'MA0000012007'},
              {'name': 'SALAFIN', 'ISIN': 'MA0000011744'},
              {'name': 'SAMIR', 'ISIN': 'MA0000010803'},
              {'name': 'SMI', 'ISIN': 'MA0000010068'},
              {'name': 'Stokvis Nord Afr', 'ISIN': 'MA0000011843'},
              {'name': 'SNEP', 'ISIN': 'MA0000011728'},
              {'name': 'SODEP', 'ISIN': 'MA0000012312'},
              {'name': 'Sonasid', 'ISIN': 'MA0000010019'},
              {'name': 'SRM', 'ISIN': 'MA0000011595'},
              {'name': 'Ste Boissons', 'ISIN': 'MA0000010365'},
              {'name': 'STROC Indus', 'ISIN': 'MA0000012056'},
              {'name': 'TAQA Morocco', 'ISIN': 'MA0000012205'},
              {'name': 'Timar', 'ISIN': 'MA0000011686'},
              {'name': 'Total Maroc', 'ISIN': 'MA0000012262'},
              {'name': 'Unimer', 'ISIN': 'MA0000012023'},
              {'name': 'Wafa Assur', 'ISIN': 'MA0000010928'},
              {'name': 'Zellidja', 'ISIN': 'MA0000010571'},
              {'name': 'MASI', 'ISIN': ''}]

tickers = [item['name'] for item in notation_code()]

def get_code(name):
    ticker_code = notation_code()
    for ticker in ticker_code :
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

	data = pd.concat(data, axis = 1, sort="False").reindex(data[0].index)
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
