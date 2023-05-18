import requests

class CurrencyConverter:

    def __init__(self):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

    def convert(self, base_currency, des_currency, amount):
        # convert from base_currency to EUR
        if base_currency != 'EUR':
            amount /= self.rates[base_currency]
        # convert from EUR to des_currency
        amount *= self.rates[des_currency]
        # Limiting the result to 2 decimal places
        amount = round(amount, 2)
        
        return amount