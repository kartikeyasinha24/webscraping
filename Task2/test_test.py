import requests
import re
import datetime
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

# titles of the sheet
sheet.append(['source_id', 'article_title', 'url', 'authors', 'author_affiliation',
              'abstract_text', 'data', 'start_time', 'end_time', 'session_title',
              'session_type', 'category', 'disclosure'])

# backpack is like a key to access the content of the webpage
headers = {'User-Agent': 'Mozilla/5.0', 'Backpack': '11f60a7d-5c6a-4124-a6f1-d0d05f81e2e0',
           'accept': 'application/json'}
r = requests.get("https://www.abstractsonline.com/oe3/Program/9256/Session/415/presentations", headers=headers).json()
# r is now a list of dictionaries where each dictionary contains information about a single presentation

base_url = "https://www.abstractsonline.com/pp8/#!/9256/presentation/"
session_type = "ePoster"

data = []

# loop through the dictionary of presentations
for i in range(len(r)):
    lis = [i]
    obj = r[i]

    article_title = "[VIRTUAL] " + (obj["Title"].replace("<b>", "")).replace("</b>", "")
    print(article_title)
    lis.append(article_title)

    url = base_url + obj["Id"]
    print(url)
    lis.append(url)

    authors_info = obj.get("AuthorBlock", "")

    # separate authors and authors_affiliation from authors_info
    authors_html = authors_info[:authors_info.find("<I>")]
    authors_affiliation_html = authors_info.partition("<I>")[2].partition("</I>")[0]
    # remove all html tahs
    authors = re.sub('<sup>.*?</sup>', '', authors_html)
    authors_affiliation = re.sub('<sup>.*?</sup>', '', authors_affiliation_html)
    print(authors)
    lis.append(authors)
    print(authors_affiliation)
    lis.append(authors_affiliation)

    # get abstract text and remove all html tags
    abstract_text = re.sub('<.*?>', '', obj["Abstract"])
    print(abstract_text)
    lis.append(abstract_text)

    # get the date from start time
    start_date_string = obj["Start"]
    xdate = start_date_string[:8]

    # data, start_time and end_time may be empty so we are using try and except block
    try:
        # converting 6/01/2021 format to June 01, 2021 format using date time module
        start_date = datetime.datetime.strptime(xdate, "%m/%d/%Y").strftime("%b %d, %Y")
    except:
        start_date = xdate
    print(start_date)
    lis.append(start_date)

    xstart_time = start_date_string[9:20]
    try:
        # converting 12 hours format to 24 hours format
        start_time = datetime.datetime.strptime(xstart_time, "%I:%M:%S %p").strftime("%H:%M")
    except:
        start_time = xstart_time

    xend_time = obj["End"][9:20]
    try:
        # converting 12 hours format to 24 hours format
        end_time = datetime.datetime.strptime(xend_time, "%I:%M:%S %p").strftime("%H:%M")
    except:
        end_time = xend_time

    print(start_time, end_time)
    lis.append(start_time)
    lis.append(end_time)

    session_title = obj["SessionTitle"]
    print(session_title)
    lis.append(session_title)

    lis.append(session_type)

    category = obj.get("SessionTitle", "")
    print(category)
    lis.append(category)

    disclosure = obj.get("DisclosureBlock", "").replace("&nbsp;<b>", "").replace("</b>", "")
    print(disclosure)
    lis.append(disclosure)

    data.append(lis)
    sheet.append(lis)
    print("-" * 300)


# save the sheet in the file
wb.save("present.xlsx")
