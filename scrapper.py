import crochet
crochet.setup()  # 
from scrapy.crawler import CrawlerRunner
from twisted.internet.defer import DeferredList
from typing import List

from countryitem_scrapper.spider import CountryItemSpider
from countryitem_scrapper.store import CountryItemStore

def get_crawl_runner():
    return CrawlerRunner(
    {
    'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
        "LOG_LEVEL" : "INFO",
        "LOG_FILE" : "./log.log"
    })

crawl_runner = get_crawl_runner()

@crochet.wait_for(timeout=28.0)
def scrape_with_crochet(stores : List[CountryItemStore], urls : List[str]):
    crawlers = []
    for store, url in zip(stores,urls):
        crawlers.append(crawl_runner.crawl(CountryItemSpider,url=url, output=store))

    return DeferredList(crawlers)

def run():
    stores = [CountryItemStore()]
    urls = ["https://scrapethissite.com/pages/simple/"]
    
    scrape_with_crochet(stores,urls)
    output = stores[0].data
    print(output[:5])
   
run()