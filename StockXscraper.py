from bs4 import BeautifulSoup
import requests

source = requests.get('https://stockx.com/air-jordan-5-retro-moonlight-2021').text
soup = BeautifulSoup(source, 'lxml')

##BuyPrice = soup.find('div', class_='<div class="chakra-stat css-1mbo1ls">')

ShoeName = soup.find("div",'class="chakra-heading css-1gbu8yz')
print(ShoeName.prettify())

##ShoeSku = soup.find