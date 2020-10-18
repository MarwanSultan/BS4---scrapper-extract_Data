import bs4 as bs
import urllib.request


data = urllib.request.urlopen('https://www.cnn.com/').read()

soup = bs.BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
    print(link.text)
print("Test Passed!!!")
