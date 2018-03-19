# -*- coding: utf-8 -*-
import scrapy
import json
from nps_geoGraphic.items import NpsGeographicItem

class GeographicSpider(scrapy.Spider):
    name = 'geoGraphic'
    allowed_domains = ['nationalgeographic.com/travel/destinations/north-america/united-states/59-national-parks-photos']
    start_urls = ['http://www.nationalgeographic.com/travel/destinations/north-america/united-states/59-national-parks-photos/']

    def parse(self, response):
        image = NpsGeographicItem()
        script_data = response.xpath('//script').extract()
        data = script_data[12].replace('<script type="text/json" data-pestle-options>', "").replace('</script>', "")
        info = json.loads(data)
        items = info['json']['items'][0]['items']
        name =[]

        for item in items:
            title = item['title']
            img_url = item['url']
            name.append(title)
            yield {
                'image_urls': [img_url],
                'title': [title]
            }
        
