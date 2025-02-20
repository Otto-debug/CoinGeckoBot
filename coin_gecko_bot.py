from logger import log_info, log_warning, log_error

import requests
import csv
import json

def save_to_json(data, filename='data/crypto_data.json'):
    """Сохраняем данные в JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        log_info(f"Данные сохранены в: {filename}")
    except Exception as e:
        log_error(f"Ошибка при сохранении JSON: {e}")

def save_to_csv(data, filename='data/crypto_data.csv'):
    """Сохраняем данные в CSV"""
    fieldnames = ["id", "symbol", "name", "current_price", "market_cap", "total_volume"]

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for coin in data:
                writer.writerow({
                    "id": coin["id"],
                    "symbol": coin["symbol"],
                    "name": coin["name"],
                    "current_price": coin["current_price"],
                    "market_cap": coin["market_cap"],
                    "total_volume": coin["total_volume"]
                })
        log_info(f"Данные сохранены в: {filename}")
    except Exception as e:
        log_error(f"Ошибка при сохранении в CSV: {e}")


def parse(url: str):
    """Функция для получения данных с API"""

    params = {
        "vs_currency": "usd",  # Можно поменять, например, на "rub"
        "order": "market_cap_desc",  # Сортировка по капитализации
        "per_page": 100,  # Сколько монет загружать (максимум 250)
        "page": 1,
        "sparkline": "false"  # Убрать график
    }

    try:
        log_info('Запрос данных с CoinGecko API...')
        response = requests.get(url=url, params=params)
        response.raise_for_status() # Проверка статуса
        data = response.json()

        if data:
            log_info(f"Успешно загружено {len(data)} криптовалют")
        else:
            log_warning("Получен пустой список данных")

        return data
    except Exception as e:
        log_error(f"Ошибка при загрузке данных: {e}")
        return []



if __name__ == '__main__':
    log_info('Бот запущен')

    crypto_data = parse(url='https://api.coingecko.com/api/v3/coins/markets')

    if crypto_data:
        save_to_json(crypto_data)
        save_to_csv(crypto_data)

    log_info('Бот завершил работу.')

