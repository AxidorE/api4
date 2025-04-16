import os
import requests


def download_image(filename, url):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f"images/{filename}", "wb") as file:
        file.write(response.content)
