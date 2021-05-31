from scrapy.exceptions import DropItem
from .item import CountryItem
from .config import Config

class CountryItemProcessorPipeline(object):

    def process_item(self, item, spider):
        return item

class CountryItemSaverPipeline(object):

    def process_item(self, item : CountryItem, spider):
        spider.output.add(item.json())
        raise DropItem