import pandas as pd
from bs4 import BeautifulSoup
import requests



all = []

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
displayid=[x for x in range(1,26)]
for i in displayid:
    link= f"https://www.sothebysrealty.com/eng/associates/{i}-pg"
    source = requests.get(link,headers=header)
    soup = BeautifulSoup(source.text, 'lxml')
    container = soup.find_all('div',class_='Entities-search__results-container')[1]
    # print(container.text.strip())
    div = container.find_all('div',class_='Entities-card__container')
    print(len(div))
    for data in div:
        address = data.find('div',class_='Entities-card__address-wrapper p2 u-color-dark-grey palm--hide').text.strip()
        # print(address)
        type = data.find('div',class_='Entities-card__advertiser h6 u-color-sir-blue palm--hide').text.strip()
        # print(type)
        title = data.find('div',class_='Entities-card__entity-title e1 u-flex__grow u-text-uppercase u-color-dark-grey').text.strip()
        # print(title)
        name = data.find('div',class_='Entities-card__entity-details u-flex u-flex__grow-shrink u-flex--column').text.strip()
        names = name.replace(address,'').replace(type,'').replace(title,'').strip()
        # print(names)
        base_url = r'https://www.sothebysrealty.com'
        website = base_url + data.find('div',class_='Entities-card__entity-details u-flex u-flex__grow-shrink u-flex--column').find('a')["href"]
        print(website)
        try:
            
            p = data.find('div',class_='Entities-card__phones u-flex__grow').text.replace('\n','').strip()
            ph = p.lstrip("O. ").lstrip("M. ")
            phone = ph.lstrip("+1 ").replace("O. +1 ",'; ').replace("O. 1.",'; ').replace("O. ",'; ').replace("O. +",';')
            phone = phone.replace("\t",'')
            
            
            # ph = p.split('O.')[-1].split("M. ")[-1].strip()
            # phone = ph.replace("+1 ",'').replace('1.','') 
        except:
            phone = ''
        print(phone)

        dictionary = {
            "Names": names,
            "Title": title,
            'Company':'Sotheby',
            'Work email':'',
            'Phone number':phone,
            'Linkedin profile':'',
            'Website': website,
            "Address": address,
            
        }
        all.append(dictionary)
    
df = pd.DataFrame(all)
df.to_csv('new_realestate.csv',index=False)
#