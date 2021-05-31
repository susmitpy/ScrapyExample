import scrapy
from .item import CountryItem, CountryLoader
from .config import Config

class CountryItemSpider(scrapy.Spider):
    name = 'countryitem'
    custom_settings = {
        'ITEM_PIPELINES': {
            'countryitem_scrapper.pipeline.CountryItemProcessorPipeline': 100,
            'countryitem_scrapper.pipeline.CountryItemSaverPipeline' : 200
        }
    }

    def __init__(self, url, output):
        self.start_urls = [
            url
        ]
        self.output = output


    def parse(self, response):
        countries = response.css(".country")
        output = []
        for country in countries:
            loader = CountryLoader(selector=country)
            loader.add_css(Config.name, ".country-name::text")

            item = loader.load_item()
            yield item