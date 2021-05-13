from scrapy.exceptions import DropItem
from .item import CountryItem
from .config import Config

class CountryItemProcessorPipeline(object):

    def process_item(self, item, spider):
        item[Config.density] = round(item[Config.population] / item[Config.area],2)
        return item

class CountryItemSaverPipeline(object):

    def process_item(self, item : CountryItem, spider):
        spider.output.add(item.json())
        raise DropItem