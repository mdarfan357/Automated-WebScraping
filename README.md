# price_track
 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mdarfan357-price-track-appstreamlit-app-tr1vmx.streamlit.app/)

## Problem 
In todays world products are available in many websites and these prices change daily with time. Due to these complexities it becomes overwhelming for an ordinary consumer to take smart decisions about their needs. In order to save users money and make it simple for any user to buy products on eCommerce platforms I have created an application that lets users track there products prices.


CI/CD
--------------- 

CI/CD (Continuous Integration and Continuous Deployment) is one of the important topics in software development. CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment.

## But what is CI/CD?
CI means new code changes to an app are regularly built, tested, and merged to a shared repository. It’s a solution to the problem of having too many branches of an app in development at once that might conflict with each other.CD means developer’s changes to an application are automatically bug tested and uploaded to a repository after which it is deployed to the cloud in the form of a webapp that people can interact with.


Solution :
--------------- 

In this project I have tried to use these concepts to built an application that gets data from an eCommerce website **daily** using CI/CD and the app displays the data pictorially in order to take better decisions about purchasing products. 

In this project I have taken an example of the iPhone 14 but these methods can be applied to any product.

The part that I love about this project is that all the components of this project are build from scratch, the data is collected daily and the data is merged together with the old data using github actions and python. we stored all the data in a csv file.


Documentation :
--------------- 
* Check out the current price at Amazon [click here](https://www.amazon.in/Apple-iPhone-14-256GB-Midnight/dp/B0BDJ6N5D6/ref=sr_1_11?crid=2GX239JVK66ZX&keywords=iphone+14&qid=1665371671&qu=eyJxc2MiOiI1LjM4IiwicXNhIjoiNS4xOSIsInFzcCI6IjMuMzcifQ%3D%3D&sprefix=iphone+1%2Caps%2C666&sr=8-11)

* Check out the current price at Flipkart [click here](https://www.flipkart.com/apple-iphone-14-midnight-256-gb/p/itmdb32e3c997112?pid=MOBGHWFH4H3MMRAA&lid=LSTMOBGHWFH4H3MMRAAO7KNHD&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=28412f92-2c72-4639-9c33-d56a23ce8398.MOBGHWFH4H3MMRAA.SEARCH&ppt=sp&ppn=sp&ssid=yhxuzzcrzk0000001665371510740&qH=860f3715b8db08cd)

* The data from these websites are collected and stored in the [prices_track.csv](../main/price_track.csv) file and this data is sent to the webapp for data visualization.

* Please note that a "0" as the product price indicates that the product is not available at the moment 

* Do visit the [web application](https://mdarfan357-price-track-appstreamlit-app-tr1vmx.streamlitapp.com/) to see the frontend of the project

*Note that the following code runs everyday automatically in order to store the changes in the product prices* 

The skills used in this project :
--------------- 
* python
* web scraping using beautifulsoup
* front end using streamlit 
* git / github for pushing and pulling data to the cloud repo
* github actions to run tasks daily 
* .yml / .yaml files to configure tasks that are run daily 

Issues :
---------------
The issue with this project would be its Scalability. In order to prepare a dataset that has all the products hosted on an eCommerce website that an ordinary consumer would need, one would require a lot of computational resources which is not available to me as a student. Most of the resources used in this project is free.
More over, there might also be other ways of doing this project.

Alternate way of doing the same data scraping would be to use an API that fetches data for you. One such API is [Amazon Price API](https://rapidapi.com/ajmorenodelarosa/api/amazon-price1/). This was the more easy way of doing the data collection process, but I choose to use web scraping and CD to create my own dataset from scratch.


