import requests
import os
from datetime import datetime
from download import download_image
from dotenv import load_dotenv


def get_nasa_epic_image(nasa_token):
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": nasa_token, "count": 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_urls = response.json()
    for epic_url in epic_urls:
        image_name = epic_url["image"]
        date_name = epic_url["date"]
        image_date = datetime.fromisoformat(date_name).strftime("%Y/%m/%d")
        epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={nasa_token}"
        download_image(f"{image_name}.png", epic_link)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    get_nasa_epic_image(nasa_token)


if __name__ == "__main__":
    main()
