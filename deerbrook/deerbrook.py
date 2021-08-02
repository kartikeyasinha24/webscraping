import pandas as pd
from bs4 import BeautifulSoup
import requests



all = []

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
#list for filling alphabets
# test_list = []
# alpha = 'a'
# for i in range(0, 26):
#     test_list.append(alpha)
#     alpha = chr(ord(alpha) + 1) 
# for i in test_list:
link=f"https://www.deerbrookproperty.com/sales-team/a"
source = requests.get(link,headers=header)
soup = BeautifulSoup(source.text, 'html.parser')
container=soup.find('div',class_="blog_sales_team_listing")
agents_det=container.find_all('div',class_="col-sm-4")
for data in agents_det:
	agent_name= data.find('strong',class_="blog_sales_team_title").text
	print(agent_name)
	title=data.find('br').next_sibling
	s=title.lstrip()
	p = data.find('span',class_="hidden-xs").text
	print(p)
	email = data.find_all('a')
	print(email)
