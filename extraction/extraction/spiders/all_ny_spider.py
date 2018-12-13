import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ParisItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class ParisSpider(CrawlSpider):
    name = 'ny'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_museums_in_New_York_City']
    custom_settings = {
        'DEPTH_LIMIT': 2,
    }

    rules = (
        Rule(LinkExtractor(allow=('Mus', ), deny=('\.jpg', '/wiki/.+:.+')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = ParisItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1//text()').extract_first()
        item['content'] = ' '.join(response.xpath("//div[@id='bodyContent']//div[@id='mw-content-text']/*/child::p[not(@*)][1]//text()").extract())
        return item
