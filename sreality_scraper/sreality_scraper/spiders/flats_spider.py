import scrapy
import json
import re


class FlatsSpider(scrapy.Spider):
    name = 'flats'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response, **kwargs):
        data = json.loads(response.body)
        flats_data = data.get('_embedded').get('estates')
        for flat in flats_data:
            yield (
                {
                    'title': re.sub(r'\s', ' ', flat.get('name')),
                    'image_url': flat.get('_links').get('images')[0].get('href'),
                }
            )
