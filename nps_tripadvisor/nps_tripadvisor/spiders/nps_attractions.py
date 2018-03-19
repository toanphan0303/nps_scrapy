# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import os
class NpsAttractionsSpider(scrapy.Spider):
    name = 'nps_attractions'
    allowed_domains = ['tripadvisor.com']
    def __init__(self):
        self.parkname =''

    def start_requests(self):
        data = json.loads(open('/Users/h/national_park_scrapy/nps_tripadvisor/nps_tripadvisor/spiders/nps_urls.json').read())
        nps_dict = dict(data)
        for key, value in nps_dict.iteritems():
            self.parkname = key
            print(key)
            print(value)
            yield Request(value, callback=self.parse, meta={'Name': key})


    def parse(self, response):
        attraction_points = response.xpath('//div[@class="listing_info"]')
        name=self.parkname.replace("_", " ")
        for point in attraction_points:
            title = point.xpath('div[@class="listing_title "]/a/text()').extract_first()
            url = point.xpath('div[@class="listing_title "]/a/@href').extract_first()
            description = point.xpath('div[@class="listing_rating"]/div[@class="popRanking wrap"]/text()').extract_first()
            activity_types = point.xpath('div[@class="tag_line"]/div[@class="p13n_reasoning_v2"]/a/span/text()').extract()
            tags = [activity_type for activity_type in activity_types]
            yield{'name':name, 'data': {'url': url, 'title': title,'description':description, 'tags':tags}}
        relative_next_url = response.xpath('//a[@class="nav next rndBtn ui_button primary taLnk"]/@href').extract_first()
        part_urls = response.url.split('/Attractions')
        absolute_next_url = str(part_urls[0])+ str(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)
