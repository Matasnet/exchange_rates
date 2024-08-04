import requests

currencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

base_currency = input("Base currency (e.g., PLN) >> ")

num_currencies = int(input("How many currencies do you want to check (maximum is 31)? >> "))

currency_list = []
if 0 < num_currencies < 31:
    for _ in range(num_currencies):
        input_currency = input('Enter currency code (e.g., EUR or USD) >> ')
        currency_list.append(input_currency)
elif num_currencies == 31:
    currency_list = currencies
else:
    print("The value entered is greater than 31 or less than 1. The full list will be considered.")
    currency_list = currencies

api_link = f"https://api.frankfurter.app/latest?from={base_currency}&to={','.join(currency_list)}"
response = requests.get(api_link)

print('\n')
if response.ok:
    data = response.json()
    exchange_rates = data["rates"]
    print(f'Exchange rate for {data['date']}')
    print(data['base'])
    for currency_code in exchange_rates:
        print(f"{currency_code} : {exchange_rates[currency_code]}")

print(f"Data Source Provider: https://www.frankfurter.app/")
print('\n')
