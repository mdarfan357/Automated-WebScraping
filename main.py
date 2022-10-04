import requests
from bs4 import BeautifulSoup
from datetime import date
from csv import writer

today = date.today()
d1 = today.strftime("%d/%m/%Y") # dd/mm/YY
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}

def get_price_from_amazon():
    url2 = "https://www.amazon.in/Apple-iPhone-14-512GB-Blue/dp/B0BDJH3V3Q/ref=sr_1_8?keywords=iphone+14&qid=1664871745&qu=eyJxc2MiOiI1LjM4IiwicXNhIjoiNS4xOSIsInFzcCI6IjMuMzcifQ%3D%3D&sr=8-8"
    req = requests.get(url2, headers=HEADERS)
    soup = BeautifulSoup(req.content,'lxml')
    print(soup)
    print("_________________________________________________")
    price = soup.find("span",class_ = "a-offscreen")
    price = price.string.replace("₹",'').replace(',','')
    price = int(float(price)) # gets current price
    return price

def get_price_from_flipkart():
    url1 = 'https://www.flipkart.com/apple-iphone-14-blue-512-gb/p/itm6f59f7f999d00?pid=MOBGHWFHYRWUSHCF&lid=LSTMOBGHWFHYRWUSHCFXIUNTH&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=search-autosuggest&iid=40d9e4bf-b8f5-47d7-810d-c5373f7d8265.MOBGHWFHYRWUSHCF.SEARCH&ppt=sp&ppn=sp&ssid=861kp9xhj40000001664802021951&qH=860f3715b8db08cd'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content,'html.parser')
    price = soup.find("div",class_ = "_30jeq3 _16Jk6d")
    price = price.string.replace("₹",'').replace(',','')
    price = int(price) 
    return price



def create_csv():
    amz_price = get_price_from_amazon()
    flip_price = get_price_from_flipkart()
    
    with open("price_track.csv",'w',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow(['Date',"Amazon price","Flipkart price"])
        mywriter.writerow([d1,amz_price,flip_price])
        
        
def append_to_csv():
    amz_price = get_price_from_amazon()
    flip_price = get_price_from_flipkart()

    with open("price_track.csv",'a',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow([d1,amz_price,flip_price])

append_to_csv()
