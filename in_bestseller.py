import requests
import csv
from bs4 import BeautifulSoup
file = open('in_book.csv', 'w')
writer = csv.writer(file)
data = ['Name', 'URL', 'Author', 'Price',
        'Number of Ratings', 'Average Rating']
writer.writerow(data)

books = []

for x in range(5):
    s = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg="
    s = s + str(x + 1)
    page = requests.get(s)
    soup = BeautifulSoup(page.content, 'html.parser')
    lis = (soup.find_all(class_="zg_itemWrapper"))
    for i in lis:
        books.append(i)
        # print(i.prettify())
name = []
url = []
author = []
nrating = []
rating = []
price = []
temp = []
for book in books:
    temp = book.find(class_="p13n-sc-truncate p13n-sc-line-clamp-1")
    if(temp != None):
        name.append(temp.get_text().strip())
    else:
        name.append("Not Available")

    temp = book.find("a", class_="a-link-normal a-text-normal")
    # for p in temp:
    # 	price.append(p.text)
    if(temp != None):
        price.append(temp.text)
    else:
        price.append("Not Available")

    temp = book.find('a', class_="a-link-normal")['href']
    # url.append("https://www.amazon.in"+temp)
    if(temp != None):
        url.append("https://www.amazon.in" + temp)
    else:
        url.append("Not Available")

    temp = book.find(class_="a-row a-size-small")
    # for t in temp:
    # 	author.append(t.text)
    if(temp != None):
        author.append(temp.text)
    else:
        author.append("Not Available")

    temp = book.find('a', class_="a-size-small a-link-normal")
    # for t in temp:
    # 	nrating.append(t)
    if(temp != None):
        nrating.append(temp.text)
    else:
        nrating.append("Not Available")
        # print(t)
    temp = book.find('span', class_="a-icon-alt")
    # for t in temp:
    # 	rating.append(t)
    if(temp != None):
        rating.append(temp.text)
    else:
        rating.append("Not Available")


for i in range(0, 100):
    data = [name[i], url[i], author[i], price[i], nrating[i], rating[i]]
    writer.writerow(data)


# print((name))
# print((price))
# print((url))
# print((author))
# print((nrating))
# print((rating))
