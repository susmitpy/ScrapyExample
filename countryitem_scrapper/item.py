from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst, Compose
from scrapy.loader import ItemLoader


class CountryItem(Item):
    name : str = Field()
    capital : str = Field()
    population : int = Field()
    area : float = Field()
    density : float = Field()

    def json(self):
        return {
            "name" : self["name"],
            "capital" : self["capital"],
            "population" : self["population"],
            "area" : self["area"],
            "density" : self["density"]
        }

class CountryLoader(ItemLoader):
    default_item_class = CountryItem
    default_output_processor = TakeFirst()
    
    name_in = Compose(lambda x: x[1])
    name_out = Compose(
            MapCompose(str.strip, str.upper),
            TakeFirst()
    )

    population_in = MapCompose(lambda x: int(x))
    area_in = MapCompose(lambda x: float(x))

