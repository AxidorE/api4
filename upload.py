import os
import telegram
from telegram.error import NetworkError
from time import sleep
from dotenv import load_dotenv

telegram_token = os.environ["TG_TOKEN"]
telegram_chat_id = os.environ["TG_CHAT_ID"]

def get_images():
    for image in os.walk("images"):
        images = image[2]
    return images


def main():
    posts_cooldown = 14400
    retry_cooldown = 20
    load_dotenv()
    images = get_images()
    while True:
        tg_token = telegram_token
        bot = telegram.Bot(token=tg_token)
        try:
            for photo in images:
                with open(f"images/{photo}", "rb") as f:
                    bot.send_photo(chat_id=telegram_chat_id, photo=f)
                sleep(posts_cooldown)
        except NetworkError:
            print("Ошибка сети, повторное подключение через 20 секунд")
            sleep(retry_cooldown)


if __name__ == "__main__":
    main()
