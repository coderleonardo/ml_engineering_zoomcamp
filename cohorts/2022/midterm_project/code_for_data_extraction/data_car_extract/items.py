# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataCarExtractItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_name = scrapy.Field()
    car_description = scrapy.Field()
    year = scrapy.Field()
    km_traveled = scrapy.Field()
    value = scrapy.Field()

