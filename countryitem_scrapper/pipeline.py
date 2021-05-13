from scrapy.exceptions import DropItem
from .item import CountryItem

class CountryItemProcessorPipeline(object):

    def process_item(self, item, spider):
        item["density"] = round(item["population"] / item["area"],2)
        return item

class CountryItemSaverPipeline(object):

    def process_item(self, item : CountryItem, spider):
        spider.output.add(item.json())
        raise DropItem