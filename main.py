import requests
from bs4 import BeautifulSoup
from datetime import date
from csv import writer

today = date.today()
d1 = today.strftime("%d/%m/%Y") # dd/mm/YY

def create_csv():
    url = 'https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=11TX6FU49ONC7&keywords=iphone+13&qid=1658583365&sprefix=iphone+1%2Caps%2C288&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUZNSDVFRENTWUMyJmVuY3J5cHRlZElkPUEwNTY0MzkzMVUwOFpCQ1hTSzBDRSZlbmNyeXB0ZWRBZElkPUEwODcyOTE2MldIV0FKM1hCR0dLVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    url1 = 'https://www.flipkart.com/soundcore-anker-life-q10-fast-charging-bluetooth-headset/p/itmc95e0c611ba87?pid=ACCFNT7RVY8AZXBF&lid=LSTACCFNT7RVY8AZXBFRIOTVZ&marketplace=FLIPKART'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content,'html.parser')
    price = soup.find("div",class_ = "_30jeq3 _16Jk6d")
    price = price.string.replace("₹",'').replace(',','')
    price = int(price) # gets current price
    
    with open("price_track.csv",'w',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow(['Date',"Product price"])
        mywriter.writerow([d1,price])
        
        
def append_to_csv():
    url = 'https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=11TX6FU49ONC7&keywords=iphone+13&qid=1658583365&sprefix=iphone+1%2Caps%2C288&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUZNSDVFRENTWUMyJmVuY3J5cHRlZElkPUEwNTY0MzkzMVUwOFpCQ1hTSzBDRSZlbmNyeXB0ZWRBZElkPUEwODcyOTE2MldIV0FKM1hCR0dLVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    url1 = 'https://www.flipkart.com/soundcore-anker-life-q10-fast-charging-bluetooth-headset/p/itmc95e0c611ba87?pid=ACCFNT7RVY8AZXBF&lid=LSTACCFNT7RVY8AZXBFRIOTVZ&marketplace=FLIPKART'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content,'html.parser')
    # prices = soup.find_all(text = "₹")
    price = soup.find("div",class_ = "_30jeq3 _16Jk6d")
    price = price.string.replace("₹",'').replace(',','')
    price = int(price) # gets current price

    with open("price_track.csv",'a',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow([d1,price])

url = 'https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=11TX6FU49ONC7&keywords=iphone+13&qid=1658583365&sprefix=iphone+1%2Caps%2C288&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUZNSDVFRENTWUMyJmVuY3J5cHRlZElkPUEwNTY0MzkzMVUwOFpCQ1hTSzBDRSZlbmNyeXB0ZWRBZElkPUEwODcyOTE2MldIV0FKM1hCR0dLVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
url1 = 'https://www.flipkart.com/soundcore-anker-life-q10-fast-charging-bluetooth-headset/p/itmc95e0c611ba87?pid=ACCFNT7RVY8AZXBF&lid=LSTACCFNT7RVY8AZXBFRIOTVZ&marketplace=FLIPKART'
req = requests.get(url1)
soup = BeautifulSoup(req.content,'html.parser')
# prices = soup.find_all(text = "₹")
price = soup.find("div",class_ = "_30jeq3 _16Jk6d")
price = price.string.replace("₹",'').replace(',','')
price = int(price) # gets current price
print(price)

append_to_csv()
