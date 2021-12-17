#dl
from bs4 import BeautifulSoup
import requests
import time
import matplotlib.pyplot as plt
import pandas as pd

cookies = {
    'TS01fb8d58': '0104881522c422daff1b995baacffcb6ce8c4ecbdcb544401df93ff04a2cc2c3dbae34adabea087572f572906ad6ee62044cac56d4832d01861578d8d9a140a9157a125a65448476511833d1c1f97e8e07fc2b4856',
    'user': 'YjA4NjA1MDQyOuadjum0u%2BaguTpzdHVkZW50OuWQjOWtuA%3D%3D',
    'PHPSESSID': '381eab8d7956d9dc0bac765b724bd45f',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'ceiba.ntu.edu.tw',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Referer': 'https://ceiba.ntu.edu.tw/',
    'Connection': 'keep-alive',
}
#.text is bad at chinese
url = requests.post('https://ceiba.ntu.edu.tw/student/', headers=headers, cookies=cookies)
soup = BeautifulSoup(url.content, 'lxml')
table_ceiba = soup.find_all('table')
table_MN = pd.read_html(url)


for info in table_ceiba:
	name = info.find_all('th')
	allinfo = info.find('td')[2]
	print(name, allinfo )



"for info in table_ceiba:
	name = info.find('td')
	print(name)
