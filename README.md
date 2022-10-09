# price_track

### Problem : 
In todays world products are available in many websites and these prices change daily with time. Due to these complexities it becomes overwhelming for an ordinary consumer to take smart decisions about their needs. In order to save users money and make it simple for any user to buy products on eCommerce platforms I have created an application that lets users track there products prices.

--------------- 
### CI/CD

CI/CD (Continuous Integration and Continuous Deployment) is one of the important topics in software development. CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. CI/CD is a solution to the problems integrating new code can cause for development and operations teams (AKA "integration hell").

### But what is CI/CD?
CI means new code changes to an app are regularly built, tested, and merged to a shared repository. It’s a solution to the problem of having too many branches of an app in development at once that might conflict with each other.CD means developer’s changes to an application are automatically bug tested and uploaded to a repository.

--------------- 
### Solution :

In this project I have tried to use these concepts to built an app that gets data from an eCommerce website daily using CI/CD and the app displays the data pictorially in order to take better decisions about purchasing products. 

In this project I have taken an example of the iPhone 14 but these methods can be applied to any product.

--------------- 
### Documentation :
Check out the current price at Amazon [click here](https://www.amazon.in/Apple-iPhone-14-512GB-Blue/dp/B0BDJH3V3Q/ref=sr_1_8?keywords=iphone+14&qid=1664871745&qu=eyJxc2MiOiI1LjM4IiwicXNhIjoiNS4xOSIsInFzcCI6IjMuMzcifQ%3D%3D&sr=8-8)

Check out the current price at Flipkart [click here](https://www.flipkart.com/apple-iphone-14-blue-512-gb/p/itm6f59f7f999d00?pid=MOBGHWFHYRWUSHCF&lid=LSTMOBGHWFHYRWUSHCFXIUNTH&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=search-autosuggest&iid=40d9e4bf-b8f5-47d7-810d-c5373f7d8265.MOBGHWFHYRWUSHCF.SEARCH&ppt=sp&ppn=sp&ssid=861kp9xhj40000001664802021951&qH=860f3715b8db08cd)

The data from these websites are collected and stored in the [prices_track.csv](../main/price_track.csv) file and this data is sent to the webapp for data visualization.

Do visit the [web application](https://mdarfan357-price-track-appstreamlit-app-tr1vmx.streamlitapp.com/) to see the frontend of the project

The skills used in this project are:
* python
* web scraping using beautifulsoup
* front end using streamlit 
* git / github for pushing and pulling data to the cloud repo
* github actions to run tasks daily 
* .yml / .yaml files to configure tasks that are run daily 



