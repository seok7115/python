import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex')
soup = bs4.BeautifulSoup(html.text,'html.parser')

doller = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print (doller.text)
