from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
	soup=BeautifulSoup(html_file,'lxml')

for job in soup.find_all('div', class_='job'):
	print(job.p)

	
