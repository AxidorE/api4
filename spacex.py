import os
import requests
from download import download_image
from dotenv import load_dotenv


def spacex_images(launch_id):
    url_space = f"https://api.spacexdata.com/v5/launches/{launch_id}"

    response = requests.get(url_space)
    response.raise_for_status()
    spacex_urls = response.json()["links"]["flickr"]["original"]
    for number, spacex_url in enumerate(spacex_urls):
        download_image(f"spacex_{number}.jpg", spacex_url)


def main():
    load_dotenv()
    launch_id = os.getenv("LAUNCH_ID", "5eb87d47ffd86e000604b38a")
    spacex_images(launch_id)


if __name__ == "__main__":
    main()