import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.google.co.kr/?hl=ko')
html = resp.text

print(html)

soup = BeautifulSoup(html, 'html.parser')
letter = soup.select('#hplogo')

print('여기부터가 진짜')

for n in letter:
    print(n['src'])
