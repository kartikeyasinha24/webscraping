from bs4 import BeautifulSoup
import requests
import csv
import datetime 
csvfile=open('isih_ext.csv','w')

csv_writer=csv.writer(csvfile)
csv_writer.writerow(['source_id','manual_id','article_title','url','authors','authors_affiliation','abstract_text','date','start_time','end_time','location','session_title','session_type','category','sub_category','disclosure','image_table'])
displayid=[1,2,3,4]
for i in displayid:
	link=f"http://www.islh.org/online/planner/program_grid_no_header.php?page=program&displayday={1}&pads=&start_range=&start_interval=&changing_days=yes"
	source = requests.get(link).text
	soup = BeautifulSoup(source, 'lxml')
	session_type = ""
	tables = soup.body.find_all('table')[2:]
	for table in tables:
		for article in soup.find_all('tr'):
			source_id=None
			manual_id=None
			try:
				art_tit=article.find('td',align='left',colspan='5').b.text #articletitle
			except Exception as e:
				art_tit=None
			
			try:
				auth=article.find('td',align='left',colspan='5').font.next_sibling.text #articletitle
			except Exception as e:
				try:
					auth=article.find('td',align='left',colspan='5').br.next_sibling
				except Exception as e:
					auth=None
			try:
					auth_aff=article.find('td',align='left',colspan='5').sup.find_next_sibling('font',size="2").next_sibling
			except Exception as e:
					auth_aff=None
			print(auth_aff)
			try:
				date1= soup.find('td',align='left',width='250').text.split(', ')
				date1=date1[1]+', '+date1[2]
			except Exception as e:
				date1=None
			location1='WORKSHOP'
			session_title = article.find_all('td')[1].div.td.font.b.text
			session_title = session_title_info.split(':')[1]
			if len(session_type):
	            session_type = session_title_info.split(':')[0]
	        else:
	            session_type += session_title_info.split(':')[0]
			print(art_tit)
			print(link)
			print(auth)
			print(auth_aff)
			print(date1)
			print(start_time)
			print(end_time)
			print(location2)
			print(session_title)
			print(session_type)
			csv_writer.writerow([])
csvfile.close()

	
	
	