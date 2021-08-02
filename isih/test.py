from bs4 import BeautifulSoup
import requests
import csv
# displayid=[1,2,3,4]
# for i in displayid:
link=f"http://www.islh.org/online/planner/program_grid_no_header.php?page=program&displayday={1}&pads=&start_range=&start_interval=&changing_days=yes"
source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
for tr in soup.find_all('tr'):
	td=tr.find_all('td')
	print(td[1].text)

