import threading
import time
import requests
from flask import Flask
from threading import Thread

# Flask сервер для поддержания активности
app = Flask('')

@app.route('/')
def home():
    return "Бот работает!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Функция для пинга бота каждые 10 минут
def ping_bot():
    while True:
        time.sleep(600)  # 10 минут
        try:
            requests.get('https://ваше-имя.onrender.com')
        except:
            pass

# Запускаем Flask и пинговальщик
keep_alive()
threading.Thread(target=ping_bot, daemon=True).start()

# Дальше ваш существующий код с ботом...
# ВАЖНО: Удалите токен из кода и используйте переменные окружения!
import os
TOKEN = os.environ.get('BOT_TOKEN')  # Токен нужно будет добавить в настройках Render