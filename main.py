from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Genghis_Khan"

result = requests.get(url).text
soup = BeautifulSoup(result, 'lxml')

frases = [i.text for i in soup.find_all('p')]
print(frases)
