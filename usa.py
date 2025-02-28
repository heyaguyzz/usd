import requests
from bs4 import BeautifulSoup

def get_usd_exchange_rate():
    url = "https://bank.gov.ua/ua/markets/exchangerates"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # знаходимо рядок з курсом USD.
    table = soup.find("table")
    rows = table.find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        if cols and "USD" in cols[1].text:
            return float(cols[2].text.replace(',', '.'))
    
    return None

def convert_currency(amount, rate):
    return round(amount / rate, 2)

def main():
    exchange_rate = get_usd_exchange_rate()
    if exchange_rate is None:
        print("Не вдалося отримати курс валют.")
        return
    
    try:
        amount = float(input("Введіть суму в гривнях: "))
        converted = convert_currency(amount, exchange_rate)
        print(f"Сума в доларах США: {converted}")
    except ValueError:
        print("Будь ласка, введіть коректне число.")

if __name__ == "__main__":
    main()
