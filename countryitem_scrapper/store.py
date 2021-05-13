from .item import CountryItem

class CountryItemStore():
    def __init__(self):
        self.data = []

    def add(self, item : CountryItem):
        self.data.append(item)