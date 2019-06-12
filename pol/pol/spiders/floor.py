# -*- coding: utf-8 -*-
import scrapy
from ..items import PolItem

class FloorSpider(scrapy.Spider):
    name = 'floor'
    allowed_domains = ['polvamvdom.ru']
    start_urls = ['https://polvamvdom.ru/laminat/']
    page_number = 2
    def parse(self, response):
        items = PolItem()
        catalog = response.xpath("//div[contains(@class, 'product short-view')]")
        for cat in catalog:
            articul = cat.xpath('.//div[contains(@class, "product-name")]//span[2]/text()').get()
            link = cat.xpath('.//div[contains(@class, "product-name")]//a/@href').get()
            price = cat.xpath('.//div[contains(@class, "product-price")]//div[@class="price"]//span/text()').getall()
            img_lnk = ''
            galery = []
            description = ''

            items['title'] = articul
            items['link'] = link
            items['price'] = price
            yield items

        next_page = response.xpath('//li[@class="next"]/a/@href').getall()[0]

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
