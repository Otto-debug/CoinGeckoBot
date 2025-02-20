# 📌 Документация: Бот для сбора данных о криптовалютах

## 📖 Описание проекта
Этот бот запрашивает данные о криптовалютах с API **CoinGecko**, затем сохраняет их в **JSON** и **CSV** форматах. Также предусмотрено логирование для отслеживания работы бота.

## 🚀 Функциональность
✅ Запрашивает данные о криптовалютах с CoinGecko API
✅ Сохраняет данные в **JSON** и **CSV** файлы
✅ Логирует ошибки и события в **bot.log** и выводит их в консоль

## 🔧 Установка
### 1️⃣ Клонируем репозиторий
```bash
git clone https://github.com/Otto-debug/CoinGeckoBot.git
cd CoinGeckoBot
```

### 2️⃣ Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

## 🔥 Использование
Запуск бота:
```bash
python coin_gecko_bot.py
```

## 📂 Структура проекта
```
Scrap-bot/
│── coin_gecko_bot.py          # Основной файл (получение и сохранение данных)
│── logger.py        # Логирование событий
│── requirements.txt  # Зависимости проекта
│── data/            # Директория для сохранения данных
│   │── crypto_data.json  # JSON-файл с криптовалютами (создаётся после запуска)
│   │── crypto_data.csv   # CSV-файл с криптовалютами (создаётся после запуска)
│── logs/            # Директория для логов
│   │── bot.log      # Файл логов (создаётся автоматически)
```

## 🔍 Основные файлы
### **1. `main.py`** – основной код бота
- Получает данные с CoinGecko API
- Логирует процесс
- Сохраняет данные в **JSON** и **CSV** (в папку `data/`)

### **2. `logger.py`** – логирование
- Записывает логи в **logs/bot.log**
- Выводит сообщения в консоль

## 📡 API CoinGecko
Бот использует **CoinGecko API** для получения данных. URL запроса:
```
https://api.coingecko.com/api/v3/coins/markets
```
Параметры:
- `vs_currency=usd` – валюта (USD)
- `order=market_cap_desc` – сортировка по капитализации
- `per_page=100` – количество криптовалют
- `page=1` – номер страницы
- `sparkline=false` – отключение графиков

## ⚠️ Возможные ошибки
| Ошибка | Решение |
|--------|---------|
| `requests.exceptions.ConnectionError` | Проверить интернет-соединение |
| `Ошибка при загрузке данных: 429 Too Many Requests` | API временно заблокировало запросы – подождите 1-2 минуты |

## 📜 Лицензия
Проект распространяется под лицензией MIT.

---

💡 **Разработчик:** [Otto / GitHub]

# CoinGeckoBot
# CoinGeckoBot
