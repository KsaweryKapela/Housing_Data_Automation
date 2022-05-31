from bs4 import BeautifulSoup
import requests

HOUSING_PAGE_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


class DataScrapping:

    def __init__(self):
        self.final_addresses = []
        self.final_prices = []
        self.final_links = []
        req_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        response = requests.get(HOUSING_PAGE_URL, headers=req_headers)
        web_page = response.text
        self.soup = BeautifulSoup(web_page, "html.parser")

    def get_price(self):
        raw_prices = self.soup.find_all("div", "list-card-price")
        self.final_prices = [price.text[:6] for price in raw_prices]

    def get_address(self):
        raw_addresses = self.soup.find_all("address", "list-card-addr")
        self.final_addresses = [address.text for address in raw_addresses]

    def get_link(self):
        data = self.soup.findAll('div', "list-card-info")
        for div in data:
            links = div.findAll('a')
            for a in links:
                self.final_links.append("https://www.zillow.com/" + a['href'])

    def get_all_info(self):
        self.get_link()
        self.get_price()
        self.get_address()

