import scrapy


class SnackSpider(scrapy.Spider):
    name = 'snacks'
    start_urls = [
        'https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/']

    def parse(self, response):
        breadcrumb = response.css('div.breadcrumb>ul>li>a::text').extract()
        yield {
            'breadcrumb': breadcrumb
        }

        for product in response.css('div.product-details'):
            name = product.css('h2::text').get()
            price = product.css('div.price::text').get().replace(
                '\n', '').replace(' ', '')
            link = product.css('a.title').attrib['href']
            yield {
                'name': name,
                'price': price,
                'link': link
            }
