import pandas as pd
from bs4 import BeautifulSoup
import os

dict1 = {
    'attorney_id': [], 'name': [], 'profile_url': [], 'address_1': [], 'address_2': [], 'city': [], 'state': [],
    'zip': [], 'country': [], 'about_descriptions': [], 'website_url': [], 'telephone_number': [],
}

header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/91.0.4472.114 Safari/537.36'}
main_folder = 'avvo'
if not os.path.exists(main_folder):
    print('file does not exist in avvo ')

fname=os.listdir(main_folder)
print(fname)

for i,file in enumerate(fname):
    f=open(main_folder+"/"+file,'r')
    soup = BeautifulSoup(f, features='lxml')
    name = soup.select('.u-vertical-margin-0')[0].text
    dict1['attorney_id'].append(i+1)
    # if the website is not there then below code if block will run
    if name == 'See lawyers by practice area':
        dict1['name'].append('')
        dict1['address_1'].append('')
        dict1['address_2'].append('')
        dict1['about_descriptions'].append('')
        dict1['website_url'].append('')
        dict1['city'].append('')
        dict1['state'].append('')
        dict1['country'].append('')
        dict1['zip'].append('')
        dict1['profile_url'].append('')
        dict1['telephone_number'].append('')
        continue
    dict1['name'].append(name)

    url = soup.select('.nav-item')[0]['href']
    dict1['profile_url'].append(url)
    try:
        address_1 = soup.select('.v-lawyer-address')[0].text
    except:
        address_1 = ""

    try:
        address_2 = soup.select('.v-lawyer-address')[1].text
    except:
        address_2 = ""

    dict1['address_1'].append(address_1)
    dict1['address_2'].append(address_2)

    try:
        address_info = soup.select('.js-v-address')[0]
        dict1['city'].append(address_info['data-city'])
        dict1['state'].append(address_info['data-state'])
        dict1['country'].append('United States')
        zip_ = ''
        try:
            address_span = address_info.span.select('p')[1].select('span')
            for info in address_span:
                print(info.text.strip(', '))
                if info.text.strip(', ').isnumeric():
                    zip_ += info.text.strip(', ')
        except:
            pass

        dict1['zip'].append(zip_)



    except:
        dict1['city'].append('')
        dict1['state'].append('')
        dict1['country'].append('')
        dict1['zip'].append('')

    try:
        section=soup.find('section',id='about')
        about=""
        try:
            d=section.find('span',class_="js-context v-specialty-display").text
        except Exception as e:
            d=''
        about+=d
        text=section.find('div',class_="sidebar-box")
        if text.find('span',id="show-more-top-practice-area-legend") is None:
            para=text.find_all('p')
            for p in para:
                s=str(p)
                s=s.replace('​'," ").replace('<br/>','\n').replace('<p>'," ").replace('</p>',' ').replace('&amp;',' ').replace('<p class="u-margin-bottom-0"><em class="small">',' ').replace('/em','\n').replace('<p class="small text-muted"> ','').replace('<p class="small text-muted">','').replace(' ','').replace('<p style="font-family:Lato , sans-serif;font-size:18px;">','').replace('<em>','').replace('<','').replace('>','')
                about+=s
        else:
            about=''
        try:
            extra_about = soup.select('.js-specialty')[0].text
            x = about.find(extra_about)
            # print('k'*100)
            # print(extra_about)
            about = about[: x]
        except:
            pass
    except:
        about = ''
    


    print(about)
    print('+'*100)
    dict1['about_descriptions'].append(about)
    try:
        website = soup.select('.text-truncate')[1].a['href']
    except:
        website = ''
    dict1['website_url'].append(website)
    try:
        phone = soup.select('.js-v-phone-replace-text')[0].text
    except:
        phone = ''
    dict1['telephone_number'].append(phone)

    # df = pd.DataFrame(dict1)
    # print(df)
    f.close()

    for key in dict1.keys():
        print(key, len(dict1[key]))

df = pd.DataFrame(dict1)
df.to_excel('avvo.xlsx',index=False)
print(df)