import os
import telegram
from telegram.error import NetworkError
from time import sleep
from dotenv import load_dotenv


def get_images():
    for image in os.walk("images"):
        images = image[2]
    return images


def main():
    load_dotenv()
    images = get_images()
    while True:
        tg_token = os.environ["TG_TOKEN"]
        bot = telegram.Bot(token=tg_token)
        try:
            for photo in images:
                with open(f"images/{photo}", "rb") as f:
                    bot.send_photo(chat_id=os.environ["TG_CHAT_ID"], photo=f)
                sleep(14400)
        except NetworkError:
            print("Ошибка сети, повторное подключение через 20 секунд")
            sleep(20)


if __name__ == "__main__":
    main()
