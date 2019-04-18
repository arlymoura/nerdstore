# -*- coding: utf-8 -*-
from main.models import Product

class NerdStorePipeline(object):
    def process_item(self, item, spider):
        p = Product()
        p.title = self.item["title"]
        p.price = float(self.item['price'].replace(',','.').strip())
        p.image = self.item['image_url'] or ''
        p.save()
        return item
    