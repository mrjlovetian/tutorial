import scrapy

from tutorial.items import TutorialItem

import os

import urllib.request

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

index = 0

class DmozSpider(scrapy.spiders.Spider):
    name = "image"
    allowed_domains = ["wall.alphacoders.com"]


    start_urls = []
    for a in range(1, 50, 1):
        page = '%s' % a
        url = 'https://wall.alphacoders.com/by_sub_category.php?id=169002&name=%E6%A8%A1%E7%89%B9+%E5%A3%81%E7%BA%B8&lang=Chinese&page=' + page
        start_urls.append(url)


    def parse(self, response):

        for sel in response.xpath("//div[@class='boxgrid']/a/img"):
            item = TutorialItem()
            global index
            # item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('@src').extract()
            # item['desc'] = sel.xpath('text()').extract()
            imageUrl = sel.xpath('@src').extract()[0]
            if not os.path.exists('images'):
                os.mkdir('images')

            fileName = "images/%s.jpg" % index
            print('***************%s%s' % (fileName, imageUrl))
            urllib.request.urlretrieve(imageUrl, fileName)
            index += 1
            yield  item