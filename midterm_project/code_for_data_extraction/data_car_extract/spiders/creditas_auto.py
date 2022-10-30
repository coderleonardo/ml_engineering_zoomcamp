import scrapy
from ..items import DataCarExtractItem

# more infos: https://docs.scrapy.org/en/latest/index.html


class CreditasAutoSpider(scrapy.Spider):
    name = 'creditas_auto'
    allowed_domains = ['auto.creditas.com']
    start_urls = cars_links = ["https://auto.creditas.com/catalogo/pagina/" + str(page) + "?sort_asc=relevance" \
            for page in range(1, 122)]
    #['https://auto.creditas.com/catalogo']


    def parse(self, response):
        item = DataCarExtractItem()
        box_address = response.xpath('//div[@id="vehicles-list"]')

        for (car_name, car_last_name, car_desc, year, km, car_value) in \
        zip(box_address.xpath('.//a/div/div[2]/div/div[1]/span[1]/text()[1]'), # car_name
            box_address.xpath('.//a/div/div[2]/div/div[1]/span[1]/text()[3]'), # car_last_name
            box_address.xpath('.//a/div/div[2]/div/div[1]/p/text()'), # car_desc
            box_address.xpath('.//a/div/div[2]/div/div[1]/span[2]/text()[1]'), # year
            box_address.xpath('.//a/div/div[2]/div/div[1]/span[2]/text()[3]'), # km_traveled
            box_address.xpath('.//a/div/div[2]/div/div[3]/div/p[3]/span/text()')): # car_value
            item["car_name"] = str(car_name.get()) + " " + str(car_last_name.get())
            item["car_description"] = car_desc.get()
            item["year"] = year.get()
            item["km_traveled"] = km.get()
            item["value"] = car_value.get()
            yield item

            # save as json: scrapy crawl creditas_auto -o cars_infos.json
            # save as csv: scrapy crawl creditas_auto -o cars_infos_creditas.csv

