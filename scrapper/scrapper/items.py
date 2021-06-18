# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

from dashboard.models import StockMarket


class ScrapeMarket(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = StockMarket