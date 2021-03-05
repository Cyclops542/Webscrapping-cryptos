from selenium import webdriver
from scrapping.domain import Domain

def main():
    binance = Domain()
    binance.initialize_search()

main()
