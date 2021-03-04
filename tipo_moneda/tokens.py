from selenium import webdriver
from .constants import tokens_stored

class Tokens:
    def __init__(self):
        self.token_type = None
        self.price = 0


    # Getters y setters
    def set_token_type(self, token_type):
        try:
            if token_type.upper() in tokens_stored:
                self.token_type = token_type
        except:
            print("There's no token in the database")
    
    def set_price(self, price):
        pass

    def get_token_type(self):
        return self.tipo_moneda

    def get_price(self):
        return self.precio
    


