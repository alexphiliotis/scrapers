import scrapy
from scrapy.crawler import CrawlerProcess
from time import sleep

class WineSpider(scrapy.Spider):
    name = 'winespider'
    start_urls = ['https://napavintners.com/wineries/all_wineries.asp']

    def parse(self, response):
        for winery in response.css('div.span_8'):
            sleep(3)
            name = winery.css('h4 >a').extract_first()
            print(f'Now scraping {name}')
            yield {
                'name': winery.css('h4 >a').extract_first(),
                'address, phone and hours': winery.css('::text').extract_first(),
                'website': winery.css('a::attr(href').extract(),
            }

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(WineSpider)
process.start()