from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp , "lxml")


# One common task is extracting all the URLs found within a page’s <a> tags:
for curA in soup.find_all('a'):
    print( curA.get('href') )
