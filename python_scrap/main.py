from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print( type(soup.title) )
# print()


# print(soup.title.attrs)
# soup.title['another_attr'] = 1
# print(soup.title)
# print(soup.title.attrs)
# del soup.title['another_attr']
# print(soup.title)
# print(soup.title.attrs)
# # print(soup.title['another_attr'])
# print()

# # print(  soup.find_all('p') )
# for curP in soup.find_all('p'):
#     print( curP , curP['class'] )
# print()


# print( soup.p ) # only first 
# print( soup.p['class'])
# print( soup.find_all('p')[0] )
# print( soup.find_all('p')[0]['class'] )
# print()

# print(soup.a)
# print(soup.find_all('a'))
# # One common task is extracting all the URLs found within a page’s <a> tags:
for curA in soup.find_all('a'):
    print( curA.get('href'))
    # print( curA.get('id') , curA.attrs)


# Another common task is extracting all the text from a page:
# print( soup.get_text() )