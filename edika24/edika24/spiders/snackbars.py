import scrapy


class SnackbarsSpider(scrapy.Spider):
    name = "snackbars"
    allowed_domains = ["www.edeka24.de"]
    start_urls = [
        "https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel"]

    def start_requests(self):
        URL = 'https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('div.product-details'):
            yield {
                'title': selector.css('h2 ::text').get(),
                'price': selector.css('div.price :: text').get()
            }

        # next_page_link = response.css('li.next a::attr(href)').extract_first()
        # if next_page_link:
        #     yield response.follow(next_page_link, callback=self.response_parser)
