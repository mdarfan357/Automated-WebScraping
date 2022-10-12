import requests
from bs4 import BeautifulSoup
from datetime import date
from csv import writer
import time

today = date.today()
d1 = today.strftime("%d/%m/%Y") # dd/mm/YY
poss_headers = ["Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
"Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",
"Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"]

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}

def get_price_from_amazon():
    ur2 = "https://www.amazon.in/Apple-iPhone-14-256GB-Midnight/dp/B0BDJ6N5D6/ref=sr_1_11?crid=2GX239JVK66ZX&keywords=iphone+14&qid=1665371671&qu=eyJxc2MiOiI1LjM4IiwicXNhIjoiNS4xOSIsInFzcCI6IjMuMzcifQ%3D%3D&sprefix=iphone+1%2Caps%2C666&sr=8-11"    
    req = requests.get(url2, headers=HEADERS)
    time.sleep(4)
    soup = BeautifulSoup(req.content,'lxml')
    price = soup.find("span",class_ = "a-offscreen")
    return price

def get_price_from_flipkart():
    url1 = 'https://www.flipkart.com/apple-iphone-14-midnight-256-gb/p/itmdb32e3c997112?pid=MOBGHWFH4H3MMRAA&lid=LSTMOBGHWFH4H3MMRAAO7KNHD&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=28412f92-2c72-4639-9c33-d56a23ce8398.MOBGHWFH4H3MMRAA.SEARCH&ppt=sp&ppn=sp&ssid=yhxuzzcrzk0000001665371510740&qH=860f3715b8db08cd'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content,'html.parser')
    price = soup.find("div",class_ = "_30jeq3 _16Jk6d")
    price = price.string.replace("₹",'').replace(',','')
    price = int(price) 
    return price



def create_csv(amz_price,flip_price):
    
    with open("price_track.csv",'w',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow(['Date',"Amazon price","Flipkart price"])
        mywriter.writerow([d1,amz_price,flip_price])
        
        
def append_to_csv(amz_price,flip_price):
   
    with open("price_track.csv",'a',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow([d1,amz_price,flip_price])
     
def check_header():
   itt = 1
   for i in poss_headers:
      amz_price = get_price_from_amazon() 
      if amz_price == None:
         HEADERS["User-Agent"] = i
         print(itt)
         itt+=1
      elif amz_price != None:
          print(f"Got header : {i}")
          amz_price = amz_price.string.replace("₹",'').replace(',','')
          amz_price = int(float(amz_price))
          flip_price = get_price_from_flipkart()      
          append_to_csv(amz_price,flip_price)
          break
      else:
            print(f"New Item : {amz_prize}")
            break
            
   
   

check_header()
     
            
