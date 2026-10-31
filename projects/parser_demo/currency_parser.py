import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def fetch_cbr_rates():
    """
    Собирает курсы валют ЦБ РФ.
    Демонстрация работы с HTTP-запросами и XML-парсингом.
    """
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    
    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching data from CBR...")
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, 'xml')
        valutes = soup.find_all('valute')
        
        data = []
        for v in valutes[:5]: # Берем первые 5 для примера
            nominal = int(v.find('nominal').text.strip())
            char_code = v.find('charcode').text.strip()
            value = float(v.find('value').text.replace(',', '.'))
            
            data.append({
                'Code': char_code,
                'Nominal': nominal,
                'Rate_per_unit': round(value / nominal, 4)
            })
            
        return data

    except Exception as e:
        print(f"Error fetching rates: {e}")
        return []

if __name__ == "__main__":
    rates = fetch_cbr_rates()
    if rates:
        print("\nTop 5 Rates:")
        for r in rates:
            print(f"{r['Code']}: {r['Rate_per_unit']} RUB/unit")
