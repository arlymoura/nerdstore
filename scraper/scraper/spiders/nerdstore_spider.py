import scrapy
from ..items import ProductItem
from main.models import Product

class NerdStoreSpider(scrapy.Spider):
    name = 'nerdstore'
    start_urls = ['https://nerdstore.com.br/categoria/especiais/game-of-thrones/']

    def parse(self, response):
        for product in response.css('.product'):
            item =  {
                'title': product.xpath('.//h2[contains(@class, "product__title")]/text()').get(),
                'price': product.xpath('.//span[contains(@class, "Price-amount")]/text()').get(),
                'image_url': product.xpath('.//img[contains(@class, "secondary-image")]/@src').get()
            }
            self.process_item(item, self)
            yield item

    def process_item(self, item, spider):
        p = Product()
        p.title = item["title"]
        p.price = float(item['price'].replace(',','.').strip())
        p.image = item['image_url'] or ''
        p.save()
        return item
