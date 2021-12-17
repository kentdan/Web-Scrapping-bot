import scrapy

class WhiskeySpider(scrapy.Spider):
	name ='whiskey'
	start_urls = ['https://www.whiskyshop.com/newreleases?item_availability=In+Stock']

	def parse(self, response):
		for products in response.css('div.product-item-info'):
			try:
				yield {
					'name': products.css('a.product-item-link::text').get(),
					'price': products.css('span.price::text').get().replace('£',''),
					'link': products.css('a.product-item-link').attrib['href'],
				}#scrappy return make dictionary
			except:
				yield {
					'name': products.css('a.product-item-link::text').get(),
					'price': 'sold out',
					'link': products.css('a.product-item-link').attrib['href'],
				}

		next_page = response.css('a.action.next').attrib['href']
		if next_page is not None:
			yield respnse.follow(next_page, callback=self.parse)
