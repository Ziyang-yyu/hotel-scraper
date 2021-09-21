import scrapy


class houseSpider(scrapy.Spider):
# This name represents the name of the crawler we want to run
    name = "houseSearch"

    start_urls = [
    #        'https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt'
    'https://www.booking.com/holiday-homes/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaHWIAQGYAQm4ARjIAQzYAQPoAQGIAgGoAgS4Ao-lpooGwAIB0gIkM2NkZDlkYzktN2Q1MC00MmJmLWI3ODMtMzkyODBhNjRhZGUz2AIE4AIB;sid=8f38d02c4fd198c2a435d8eb2493255f;from_booking_home_promotion=1;srpvid=ae3d3a04a34a009f&'
        ]
   
   # Content of the page is inside response
    def parse(self, response):
        # Select all the wanted elements
        for link in response.css("ul.bui-carousel__inner>li.bui-carousel__item div.bui-card__content > a::attr('href')"):
            yield scrapy.Request(url='https://www.booking.com'+link.get(), callback=self.parseContent)
      
    def parseContent(self, response):
        print(response.text)
      
    
   
        