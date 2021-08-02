from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://www.islh.org/online/planner/program_grid_no_header.php?page=program&displayday=1&pads=&start_range=&start_interval=&changing_days=yes').text

soup = BeautifulSoup(source, 'lxml')
# csvfile=open('cms_scrape.csv','w')

# csv_writer=csv.writer(csvfile)
# csv_writer.writerow(['headline','summary','videolink'])

# for article in soup.find_all('article'):
# 	headline=article.h2.a.text
# 	print(headline)

# 	summary=soup.find('div',class_='entry-content').p.text
# 	print(summary)

	

# 	try:
# 		vidsrc=article.find('iframe', class_="youtube-player")['src']
# 		vid_id=vidsrc.split('/')[4]
# 		vid_id=vid_id.split('?')[0]
# 		# print(vid_id)
# 		yt_link = f"https://www.youtube.com/watch?v={vid_id}"
		
# 	except Exception as e:
# 		yt_link=None
	
# 	print(yt_link)
# 	print()
# 	csv_writer.writerow([headline,summary,yt_link])
# csvfile.close()

print(source)