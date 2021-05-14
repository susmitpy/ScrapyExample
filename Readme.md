# Scrapy Code Generator With Example
# Components
1. Custom Item
2. Custom Item Loader
3. Pipelines
4. Processor Class
5. Saver Class
6. Item Store
7. Config (Keep the name of the properties of item being scraped consistent)
8. Logging into a log file (remaining)

## How to see demo ?
1. Install requirements in requirements.txt
2. Run scrapper.py
3. Explore The Code

url being scraped : https://scrapethissite.com/pages/simple/

## How to start new project ?
1. Run gen_scrapper.py
2. Say yes to create a scrapper.py if no spiders already exists
3. Type the name of the item to be scraped (eg: Country, YoutubePlaylist, QuoraQuestion, etc) 
4. Things to configure:
    - Config class in config.py
    - parse function in spider.py
    - item & item loader in item.py
    - processor in pipeline (if you need it) in pipeline.py
5. Get Going, You Rock !


