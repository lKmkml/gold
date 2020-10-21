import requests
from bs4 import BeautifulSoup
url="https://www.goldtraders.or.th/default.aspx"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'html.parser')
find_word = soup.find_all("b")
print(find_word)