import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess


options = webdriver.ChromeOptions()
options.headless = True

url = 'https://www.casablanca-bourse.com/bourseweb/en/Listed-Company.aspx'

browser = webdriver.Chrome('/usr/bin/chromedriver', options=options)

browser.get(url)
table = browser.find_element(By.XPATH, value = '/html/body/form/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td[3]/div/table/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table')

df = pd.read_html(table.get_attribute('outerHTML'), skiprows = 1)[0]
df.to_csv("../data/companies_isin.csv")

subprocess.call("./clean_isin.sh")
