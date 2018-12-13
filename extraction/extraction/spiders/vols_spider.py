import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class VolsItem(scrapy.Item):
    dep = scrapy.Field()
    arr = scrapy.Field()
    prix = scrapy.Field()
    comp = scrapy.Field()
    duree = scrapy.Field()


class VolsSpider(scrapy.Spider):
    name = "vols"

    def start_requests(self):
        urls = [
            'http://www.google.fr/flights#flt=/m/05qtj./m/02_286.2019-01-04;c:EUR;e:1;sd:1;t:f;tt:o',
            'http://www.google.fr/flights#flt=/m/02_286./m/05qtj.2019-01-04;c:EUR;e:1;sd:1;t:f;tt:o',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = VolsItem()
        item['dep'] = response.css
        item['arr'] = response.xpath('//h1//text()').extract_first()
        item['prix'] = ' '.join(response.xpath("//div[@id='bodyContent']//div[@id='mw-content-text']/*/child::p[not(@*)][1]//text()").extract())
        return item

