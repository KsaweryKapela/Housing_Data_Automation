from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from scrapping_data import DataScrapping
import time
from dotenv import load_dotenv
import os

load_dotenv()
FORMS_LINK = os.getenv("forms_link")
DRIVER_PATH = os.getenv("driver_location")


class FillForms:

    def __init__(self):
        self.data = DataScrapping()
        chrome_driver_path = DRIVER_PATH
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def fill_all_forms(self):
        self.driver.get(FORMS_LINK)
        time.sleep(2)

        for item in range(0, len(self.data.final_links)):
            address_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                                                        '/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
                                                                      '/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
                                                                     '/div/div/div[2]/div/div[1]/div/div[1]/input')

            address_field.send_keys(self.data.final_addresses[item])
            price_field.send_keys(self.data.final_prices[item])
            link_field.send_keys(self.data.final_links[item])

            time.sleep(1)
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

            time.sleep(1)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

            time.sleep(1)





