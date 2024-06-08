import sys
from bs4 import BeautifulSoup
import requests
sys.stdout.reconfigure(encoding='utf-8')

url = "https://codeforces.com/profile/AnshulKumarNeekhara" 
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')



name = soup.find_all(class_='rated-user')[-1]
rank , rating , max_rating , max_rank  = soup.find_all('span')[18:22]
print( '{} ( {} - {} ) with maximum rank and rating ( {} - {} )'.format( name.text , rank.text , rating.text , max_rank.text[0:-2] ,  max_rating.text[-5:-1]) )

# print(name.text)
# print(rank.text)
# print(rating.text)
# print(max_rating.text[-5:-1])
# print(max_rank.text[0:-2])
# print( name.text , "(" , rank.text, "-" ,  rating.text , ")" , "with maximum" , "(" , max_rank.text[0:-2] , "-" ,  max_rating.text[-5:-1] , ")" )








# links = soup.find_all('a')
# print( len(links))

# for a in links[0:10]:
#     # print(a)
#     print(a.text)

# rank = soup.find_all(class_='user-rank')[0]
# print(rank.text)

