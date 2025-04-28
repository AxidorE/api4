import os
import requests
from urllib.parse import unquote, urlparse
from download import download_image
from dotenv import load_dotenv

def get_extension(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    path, fullname = os.path.split(parsed_url.path)
    filename, extension = os.path.splitext(fullname)
    return filename, extension


def get_nasa_apod_images(nasa_token):
    count = 30
    url = f"https://api.nasa.gov/planetary/apod"
    params = {"api_key": nasa_token, "count": count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_urls = response.json()
    for nasa_url in nasa_urls:
        if nasa_url.get("media_type") == "image":
            nasa_image = nasa_url["hdurl"] or nasa_url["url"]
        filename, extension = get_extension(nasa_image)
        download_image(f"{filename}{extension}", nasa_image)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    get_nasa_apod_images(nasa_token)


if __name__ == "__main__":
    main()
