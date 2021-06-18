# Stock-Scrapper ``` Django``` ```Scrapy```
Scrapping NSE website data and storing data into our database and serving in our a website

## Prerequisites
Python3, virtualenv en pip installed on your system. 
![NSE - Google Chrome 18-06-2021 12_50_04](https://user-images.githubusercontent.com/57286404/122522703-dfb4a700-d033-11eb-8a1a-adfd875d9086.png)

![NSE - Google Chrome 18-06-2021 12_50_13](https://user-images.githubusercontent.com/57286404/122522725-e511f180-d033-11eb-969b-3dc3af06e1df.png)
```Architecture```
![0_26rEcLHEhdXBwZE2](https://user-images.githubusercontent.com/57286404/122520948-e0e4d480-d031-11eb-9cdc-c2b5ab873992.png)
![NSE - Google Chrome 18-06-2021 12_50_26](https://user-images.githubusercontent.com/57286404/122522720-e3482e00-d033-11eb-8e1e-cc66be7ffe20.png)

![NSE - Google Chrome 18-06-2021 12_50_32](https://user-images.githubusercontent.com/57286404/122522718-e2af9780-d033-11eb-8c66-8f93bf2820de.png)
```Scrapper```
![crawller py - internship - Visual Studio Code 18-06-2021 12_34_54](https://user-images.githubusercontent.com/57286404/122520900-d32f4f00-d031-11eb-8e8d-e99dd8d9122e.png)


## How to run it?
1. Download zip fie
2. Go to the folder with ```cd Stock-Scrapper-main```
3. Create 'python -m venv env' and Activate the virtualenv: ```.env\Scripts\activate```
4. Download required files use ```pip install -r requirements.txt```
5. Now run your server with ```cd NSEscrapper_app -> python ./manage.py runserver```
6. Website running on localhost, port 8000.

## How to scrape new data ?
1. Go to the "spider" folder inside 'scrapper' and run ```scrapy runspider crawller.py```
2. New Model is updated.
3. Now run your server inside NSEscrapper_app with ```python ./manage.py runserver```
