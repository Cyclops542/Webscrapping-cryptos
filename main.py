from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def main():
    driver.get("https://www.binance.com/en")
    driver.find_element_by_id("__APP")

main()
