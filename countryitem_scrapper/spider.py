import scrapy
from scrapy.loader import ItemLoader

from .item import CountryItem, CountryLoader

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
            loader.add_css("name", ".country-name::text")
            loader.add_css("capital", ".country-capital::text")
            loader.add_css("population", ".country-population::text")
            loader.add_css("area", ".country-area::text")

            quote_item = loader.load_item()
            self.logger.info(quote_item["name"])
            yield quote_item