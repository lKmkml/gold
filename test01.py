import requests
from bs4 import BeautifulSoup
url="https://www.goldtraders.or.th/AvgPriceList.aspx"

def january():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มกราคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def febuary():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กุมภาพันธ์')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def march():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มีนาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def april():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('เมษายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def may():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('พฤษภาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def june():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('มิถุนายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def july():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กรกฎาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def august():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('สิงหาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def september():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('กันยายน')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)
def october():
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'html.parser')
    find_word = soup.find_all("table",{"id":"DetailPlace_MainGridView"},"tbody")
    for i in find_word:
        i=str(i).split('ตุลาคม')[1]
        i=str(i).split('</font>')[1]
        i=str(i).split('<td align="right"><font color="Black" face="Tahoma,Verdana" size="1">')[1]
        i=str(i).split(',')
        i=i[0]+i[1]
        return float(i)

month=[]

month.append(january())
month.append(febuary())
month.append(march())
month.append(april())
month.append(may())
month.append(june())
month.append(july())
month.append(august())
month.append(september())
month.append(october())
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates= eval(response.text)["rates"]
rateusd=[]
print(month)
for i in month :
    ex='%.2f' %(exchange_rates["USD"]*i)
    rateusd.append(ex)

rateusd =[float(i) for i in rateusd]
print(rateusd)