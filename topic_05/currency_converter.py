import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(url)
data = response.json()

rates = {item['cc']: item['rate'] for item in data if item['cc'] in ['EUR', 'USD', 'PLN']}

currency = input("Enter the currency (EUR, USD, PLN): ").upper()
amount = float(input("Enter the amount to convert: "))

if currency in rates:
    result = amount * rates[currency]
    print(f"{amount} {currency} = {result:.2f} UAH (rate: {rates[currency]:.2f})")
else:
    print("Unknown currency. Available options: EUR, USD, PLN.")
