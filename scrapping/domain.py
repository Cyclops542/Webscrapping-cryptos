from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Domain:
    def __init__(self):
        self.url = "https://www.binance.com/en"

    def initialize_search(self):
        if (self._validation_PATH("C:\Program Files (x86)", "chromedriver.exe") != None):
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            driver.get(self.url)
            try:
                main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1wr4jig")))
                crypto_combobox = main.find_element_by_class_name("css-1imen1g")
                crypto_tags = crypto_combobox.find_elements_by_tag_name("a")
                for i in range(len(crypto_tags)-1):
                    header = crypto_tags[i].find_element_by_class_name("css-1q7503z")
                    print(header.text)
            except:
                driver.quit()
            

    def _validation_PATH(self, PATH, name):
        try:
            for root, dirs, files in os.walk(PATH):
                if name in files:
                    return os.path.join(root, name)
                else:
                    return None
        except:
            print("Chromedriver is not located in Program Files (x86), make sure to fix PATH")
            return False
        
        


        