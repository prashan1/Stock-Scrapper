# Stock-Scrapper
Scrapping NSE website and storing data into django model and eventually building a website

## Prerequisites
Python3, virtualenv en pip installed on your system. 

![NSE - Google Chrome 18-06-2021 01_01_22](https://user-images.githubusercontent.com/57286404/122512217-2a2f2700-d026-11eb-8230-79a3c0bc4eaa.png)
![NSE - Google Chrome 18-06-2021 01_01_30](https://user-images.githubusercontent.com/57286404/122512215-28fdfa00-d026-11eb-956d-8fa0aa9ab007.png)
![NSE - Google Chrome 18-06-2021 01_01_38](https://user-images.githubusercontent.com/57286404/122512212-28656380-d026-11eb-9c98-ca3ebec2c77b.png)
![NSE - Google Chrome 18-06-2021 01_01_43](https://user-images.githubusercontent.com/57286404/122512206-26030980-d026-11eb-905a-8d87251e0f7a.png)


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
