import requests
from bs4 import BeautifulSoup

URL = input("Which url should scrape?   ")
srcape_type = input("What element do you want to scrape?    ")

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

print("Webscarape result:\n")
counter = 1
for s in soup.findAll(srcape_type):
    print(str(counter) + '. ' + s.get_text().strip())
    counter += 1
