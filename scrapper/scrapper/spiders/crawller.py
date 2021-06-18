import scrapy
import json
from dashboard.models import StockMarket
from scrapper.items import ScrapeMarket

class CrawllerSpider(scrapy.Spider):
    name = 'crawller'
    start_urls = ['https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY']

    # Required attributes for the table
    validAtributes = ["askPrice","askQty","bidQty","bidprice","change","changeinOpenInterest","impliedVolatility","lastPrice","openInterest","totalTradedVolume" ]
    
    def parse(self, response):
        StockMarket.objects.all().delete()
        data = json.loads(response.text)
        
        # scraping our data and storing in our model
        for i in range(92):
            marketObj = ScrapeMarket()
            newD = {"CEtotOI" : data['filtered']['CE']['totOI'],
                "CEtotVoi" : data['filtered']['CE']['totVol'],
                "PEtotOI" : data['filtered']['PE']['totOI'],
                "PEtotVoi" : data['filtered']['PE']['totVol'],
                }
            # Checking if CE is absent in data 
            try:
                newD.update({ f'ce{valid}': data['filtered']['data'][i]['CE'][valid]    for valid in self.validAtributes  })
                newD.update({'strikePrice':data['filtered']['data'][i]['CE']['strikePrice']})
            except Exception as e : 
                newD.update({ f'ce{valid}': 0.00    for valid in self.validAtributes  })

            # Checking if PE is absent in data

            try:
                newD.update({'strikePrice':data['filtered']['data'][i]['PE']['strikePrice']})
                newD.update({ f'pe{valid}': data['filtered']['data'][i]['PE'][valid]    for valid in self.validAtributes  })
            except Exception as e : 
                newD.update({ f'pe{valid}': 0.00    for valid in self.validAtributes  })

            for dataitem in newD:
                marketObj[dataitem] = newD[dataitem]  
            yield marketObj 
