import pandas as pd
from bs4 import BeautifulSoup
import requests
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

link=f"https://www.deerbrookproperty.com/sales-team/a"
source = requests.get(link,headers=header)
soup = BeautifulSoup(source.text, 'html.parser')
container = soup.find_all('div',class_= 'col-lg-6 agent-data')
for data in container:
    # email = data.find('i',class_='fa fa-fw fa-envelope text-muted').findNext('a')["href"]
    email = data.find_all('a')
    print(email)