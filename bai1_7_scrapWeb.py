#import the library used to query a website
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
print(soup.title.string)
# #print(soup.a)
# all_link = soup.find_all('a')
# for link in all_link:
#     print(link.get('href'))
all_tables = soup.find_all('table')
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
#print(right_table)
# List
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
#import pandas to convert list to data frame

df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
# Saving the file as CSV.
df.to_csv('E:/Document_Python/csv/data.csv')