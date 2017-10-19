import scrapy

from tutorial.items import TutorialItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/BigFishFly/p/6380024.html"]


    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = TutorialItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield  item