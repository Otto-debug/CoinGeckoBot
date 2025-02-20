import logging

# Создание логгера
logger = logging.getLogger("crypto_bot")
logger.setLevel(logging.INFO)

# Формат логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Логирование в файл
file_handler = logging.FileHandler('logs/bot.log', encoding='utf-8')
file_handler.setFormatter(formatter)

# Логирование в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Добавляем обработчик
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Функции
def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)
