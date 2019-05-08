import urllib
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

# url that we are scraping
url = "file:///C:/Users/David/Desktop/RealGM-Draft.html"

# this is the html from the given url
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

columns = ['Pick', 'Player', 'Team', 'Draft Trades', 'Pos', 'HT', 'WT', 'Age', 'YOS',
           'Pre-Draft Team', 'Class', 'Nationality']

df = pd.DataFrame(columns = columns)

#create table with scraped data
table = soup.find('tbody', {'class': 'tablesaw'}).table

#creating the dataframe using pandas
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index = columns), ignore_index = True)  #create a dataframe with rows and columns that are indexed as column headers


df.to_excel('nba 2018 draft.xlsx', index = False)

