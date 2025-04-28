import os
import requests


def download_image(filename, url, params=None):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(f"images/{filename}", "wb") as file:
        file.write(response.content)
