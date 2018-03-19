# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class NpsGeographicPipeline(ImagesPipeline):
    def set_filename(self, response):
        print ('response.meta= {0}'.format(response.meta))
        return 'full/{0}.jpg'.format(response.meta['title'][0])

    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'title': item['title']})

    def get_images(self, response, request, info):
        for key,image, buf in super(NpsGeographicPipeline,self).get_images(response, request,info):
            print('key: {0},image: {1}, buf:{2}'.format(key, image,buf))
            key = self.set_filename(response)
        yield key, image, buf
