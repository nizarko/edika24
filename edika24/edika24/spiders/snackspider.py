import scrapy


class SnackSpider(scrapy.Spider):
    name = 'snacks'
    start_urls = [
        'https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/']

    def parse(self, response):
        breadcrumb = []
        d = {}
        for bread in response.css('div.breadcrumb'):
            breadcrumb.append(bread.css('a::text').get())
        d = {'breadcrumb': breadcrumb}
        for product in response.css('div.product-details'):
            d = {
                'name': product.css('h2::text').get(),
                'price': product.css('div.price::text').get().replace('\n', '').replace(' ', ''),
                'link': product.css('a.title').attrib['href']
            }
        yield d
