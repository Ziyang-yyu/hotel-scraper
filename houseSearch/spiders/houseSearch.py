import scrapy


class houseSpider(scrapy.Spider):
# This name represents the name of the crawler we want to run
    name = "houseSearch"

    start_urls = [
    'https://www.booking.com/holiday-homes/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaHWIAQGYAQm4ARjIAQzYAQPoAQGIAgGoAgS4Ao-lpooGwAIB0gIkM2NkZDlkYzktN2Q1MC00MmJmLWI3ODMtMzkyODBhNjRhZGUz2AIE4AIB;sid=8f38d02c4fd198c2a435d8eb2493255f;from_booking_home_promotion=1;srpvid=ae3d3a04a34a009f&'
        ]
   
   # Content of the page is inside response
    def parse(self, response):
        # Select all the wanted elements
        for link in response.css("ul.bui-carousel__inner>li.bui-carousel__item div.bui-card__content > a::attr('href')"):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback=self.parseContent)
      
    def parseContent(self, response):
        # Get the data
        score = response.css("span.review-score-badge::text").get()
        price = response.css("div.bui-price-display__value::text").get()
        locat = response.css("p.bui-card__text::text").get()
        links = []
        for link in response.css("div.sr__card_cta_row > a::attr('href')"):
            links.append(response.urljoin(link.extract()))
        
        # Create an object to store the data
        hotelData={}
      
        hotelData['Review Score'] = score
        hotelData['Minimum Price per night'] = price
        hotelData['Location'] = locat
        hotelData['href'] = links

        print(hotelData)
