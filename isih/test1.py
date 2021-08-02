# Library for opening url and creating 
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint
import pandas as pd
# for parsing all the tables present 
# on the website
from html_table_parser.parser import HTMLTableParser
# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()
# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()
xhtml = url_get_contents('http://www.islh.org/online/planner/program_grid_no_header.php?page=program&displayday=1&pads=&start_range=&start_interval=&changing_days=yes"').decode('utf-8')
 
# Defining the HTMLTableParser object
p = HTMLTableParser()
 
# feeding the html contents in the
# HTMLTableParser object
p.feed(xhtml)
 
# Now finally obtaining the data of
# the table required
pprint(p.tables[1])
 
# converting the parsed data to
# datframe
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[1]))